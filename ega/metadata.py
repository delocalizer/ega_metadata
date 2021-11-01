"""
Utility functions to construct the necessary metadata for an EGA submisssion
from input file paths and info from the db.
"""
from dataclasses import dataclass, field, fields
from pathlib import Path
from string import Template

import importlib.resources as pkg_resources
import logging

import pysam

import graflipy.query
from graflipy import get_config
from graflipy.connect import do_query
from graflipy.ega import MetadataConstructionError
from graflipy.ega.schema_1_5_0 import (AnalysisFileType,
                                       AnalysisFileTypeChecksumMethod,
                                       AnalysisFileTypeFiletype,
                                       AnalysisType,
                                       AnalysisSet,
                                       AttributeType,
                                       Datasets,
                                       DatasetType,
                                       LinkType,
                                       ReferenceAssemblyType,
                                       ReferenceSequenceType,
                                       SampleSet,
                                       SampleType,
                                       SubmissionSet,
                                       SubmissionType)
from graflipy.reference import ReferenceAssembly, Species
from graflipy.util import get_md5

BAM_NOTE = 'SAMPLE_REF label attribute contains csv list of bam @RG IDs'
CONF = get_config()

ERR_DATASET_POLICY = 'policy_accession must be supplied iff is_icgc is False'
ERR_DBMETA_NONE = 'db metadata not found for %s'
ERR_DBMETA_MULTI = 'multiple records for db metadata for %s'
ERR_SAMPLE_INCOMPLETE = 'donor:%s collectedsample:%s - missing db data for %s'
ERR_UNKNOWN_SEQ = '%s header contains SQ not defined in the reference %s: %s'

LOGGER = logging.getLogger(__name__)


@dataclass
class DbMetaBam:
    """
    Helper to organize bam metadata query results
    """
    bam_type: str
    bam_uuid: str
    ega_accession: str
    sample_uuid: str
    library_capture_kit: str
    sequencing_platform: str
    reference: ReferenceAssembly


@dataclass
class DbMetaSample:
    """
    Helper to organize sample metadata query results
    """
    sample_uuid: str
    sample_publication_id: str
    ega_accession: str
    reference_species: Species
    sample_type: str
    sample_material: str
    sample_tissue: str
    donor_uuid: str
    donor_publication_id: str
    donor_sex: str
    phenotype: str = field(init=False)

    def __post_init__(self):
        """
        1. Ensure all fields not explicitly whitelisted are not None
        2. Set self.phenotype value
        """
        allow_none = ('ega_accession', 'phenotype')
        nonevals = [field.name for field in fields(self) if
                    field.name not in allow_none and
                    getattr(self, field.name) is None]
        if nonevals:
            raise MetadataConstructionError(
                ERR_SAMPLE_INCOMPLETE % (
                    self.donor_uuid, self.sample_uuid, ', '.join(nonevals)))
        self.phenotype = '|'.join((self.sample_tissue, self.sample_type))


def dbmeta_bam(path):
    """
    Fetch some metadata about a bam from the database

    Args:
        path: value of :filePath property to match

    Returns:
        DbMetaBam

    Raises:
        MetadataConstructionError if the specified bam is not found in the
            database, or multiple matches are found
    """
    query = Template(
        pkg_resources.read_text(graflipy.query, 'ega_meta_bam.sparql')
    ).substitute(bamPath=path)
    results = list(do_query(query))
    nresults = len(results)
    if nresults == 0:
        raise MetadataConstructionError(ERR_DBMETA_NONE % path)
    if nresults > 1:
        raise MetadataConstructionError(ERR_DBMETA_MULTI % path)
    result = results[0]
    return DbMetaBam(
        bam_type=result.type,
        bam_uuid=result.bamUuid.value,
        ega_accession=(result.egaAccession and result.egaAccession.value),
        sample_uuid=result.sampleUuid.value,
        library_capture_kit=result.libraryCaptureKit.value,
        sequencing_platform=result.sequencingPlatform.value,
        reference=ReferenceAssembly.fromstr(result.reference.value))


def dbmeta_sample(uuid):
    """
    Fetch some metadata about a sample from the database

    Args:
        uuid: UUID string of the CollectedSample

    Returns:
        DbMetaSample

    Raises:
        MetadataConstructionError if the specified sample is not found in the
            datbase, multiple matches are found, or the sample metadata is
            incomplete.
    """
    query = Template(
        pkg_resources.read_text(graflipy.query, 'ega_meta_sample.sparql')
    ).substitute(sampleUuid=uuid)
    results = list(do_query(query))
    # at least 1 result because of agg function even when no other bindings
    result = results[0]
    if not result.sampleUuid:
        raise MetadataConstructionError(
                ERR_DBMETA_NONE % ('collectedsample:'+uuid))
    if len(results) > 1:
        raise MetadataConstructionError(
                ERR_DBMETA_MULTI % ('collectedsample:'+uuid))

    return DbMetaSample(
        sample_uuid=result.sampleUuid,
        sample_publication_id=(
            result.samplePublicationID and result.samplePublicationID.value),
        ega_accession=(
            result.egaAccession and result.egaAccession.value),
        reference_species=(None if not result.referenceSpecies else
                           Species.fromstr(result.referenceSpecies.value)),
        sample_type=(
            result.sampleType and result.sampleType.value),
        sample_material=(
            result.sampleMaterial and result.sampleMaterial.value),
        sample_tissue=result.sampleTissue,
        donor_uuid=result.donorUuid,
        donor_publication_id=(
            result.donorPublicationID and result.donorPublicationID.value),
        donor_sex=(result.donorSex and result.donorSex.value))


###############################################################
# functions that return graflipy.ega.schema_1_5_0 dataclasses #
###############################################################

# xsdata XmlSerializer has a behaviour where dataclasses like Analysis that
# inherit from another dataclass (AnalysisType) get serialized as tags with an
# `xsi:type` attribute - although only when they're more than one level deep
# in the tree. Not sure if that's correct XML usage or a quirk with xsdata,
# but in either case we don't want those xsi:type attributes because the
# resulting XML doesn't validate at EGA, giving 'Invalid xsi:type qname:
# "ANALYSIS"' error.
#
# We have a workaround available though because the base class AnalysisType
# contains all we need, and doesn't serialize with the xsi:type attribute. The
# same goes for Dataset/DatasetType, Sample/SampleType, and Submission/
# SubmissionType, which is why we create and return instances of the *Type
# classes in functions below.
#
# One wrinkle to be aware of in creating test cases is that naked instances of
# these serialize with CamelCase tag names, e.g. `<AnalysisType>`. In practice
# when crafting submissions to EGA this doesn't matter because when situated
# in their appropriate container, e.g. AnalysisSet they serialize with the
# expected caps tag names i.e. `<ANALYSIS>`.

def analysis_refalign(path, md5, gpgmd5, egastudy, egadir, nodbref=None):
    """
    Returns a `graflipy.ega.schema_1_5_0.AnalysisType` instance representing an
    `ANALYSIS/ANALYSIS_TYPE/REFERENCE_ALIGNMENT` element

    Args:
        path: path to a bam on a locally accessible filesystem; also used
            as the lookup key for the bam `:filePath` property in the db.
        md5: md5 of the bam at `path`
        gpgmd5: md5 of the encrypted bam
        egastudy: EGA accession of the study the bam belongs to
        egadir: directory in the EGA upload box that contains/will contain
            the encrypted bam
        nodbref: Optional[ReferenceAssembly]. If this is supplied then the
            database is not queried for any metadata. A warning is logged and
            empty string '' is used for all corresponding properties. The
            resulting XML won't validate at EGA - it does not have any info
            about the parent sample of analsis elements, for a start - but
            this can be useful for building scaffold XML files to be manually
            completed

    Raises:
        MetadataConstructionError if the specified bam is not found in the
            database, or multiple matches are found
        ValueError if @SQ lines in the bam header are inconsistent with the
            specified reference assembly
    """
    LOGGER.info('building metadata for bam %s', path)

    if nodbref:
        LOGGER.warning('using empty db metadata for bam %s', path)

    # meta from the db
    dbmeta = (
        DbMetaBam('', '', None, '', '', '', nodbref) if nodbref
        else dbmeta_bam(path))

    # meta from the bam header
    header = pysam.AlignmentFile(path).header
    # pylint: disable=unsubscriptable-object
    readgroup_ids = [rg['ID'] for rg in header['RG']]
    sequence_names = {seq['SN'] for seq in header['SQ']}
    # pylint: enable=unsubscriptable-object

    # sanity check
    reference_sequence_names = {seq.name for seq in dbmeta.reference.sequences}
    diff = sequence_names - reference_sequence_names
    if diff:
        raise ValueError(ERR_UNKNOWN_SEQ % (path, dbmeta.reference.name, diff))

    path = Path(path)
    egadir = Path(egadir)
    root = Path('/')
    bamfilename = path.name
    submissionfilename = bamfilename + '.gpg'
    submissionfilepath = root.joinpath(
        egadir, submissionfilename).relative_to(root)

    return AnalysisType(
        alias=dbmeta.bam_uuid,
        accession=dbmeta.ega_accession,
        title=bamfilename,
        description=dbmeta.bam_type,
        study_ref=AnalysisType.StudyRef(
            accession=egastudy
        ),
        sample_ref=[
            AnalysisType.SampleRef(
                label=','.join(readgroup_ids),
                refname=dbmeta.sample_uuid
            )
        ],
        analysis_type=AnalysisType.AnalysisType(
            reference_alignment=ReferenceSequenceType(
                assembly=ReferenceAssemblyType(
                    standard=ReferenceAssemblyType.Standard(
                        accession=dbmeta.reference.accession
                    )
                ),
                sequence=[
                    ReferenceSequenceType.Sequence(
                        accession=seq.accession,
                        label=seq.name
                    ) for seq in sorted(dbmeta.reference.sequences)
                ]
            )
        ),
        files=AnalysisType.Files(
            file=[
                AnalysisFileType(
                    filename=submissionfilepath,
                    filetype=AnalysisFileTypeFiletype.BAM,
                    checksum_method=AnalysisFileTypeChecksumMethod.MD5,
                    checksum=gpgmd5,
                    unencrypted_checksum=md5
                )
            ]
        ),
        analysis_attributes=AnalysisType.AnalysisAttributes(
            analysis_attribute=[
                AttributeType(tag='NOTE', value=BAM_NOTE),
                AttributeType(tag='LibraryCaptureKit',
                              value=dbmeta.library_capture_kit),
                AttributeType(tag='SequencingPlatform',
                              value=dbmeta.sequencing_platform),
                AttributeType(tag='ReferenceSpecies',
                              value=dbmeta.reference.species.scientific_name),
                AttributeType(tag='Reference', value=dbmeta.reference.name),
            ]
        )
    )


def analysisset(paths, md5dir, egastudy, egadir, nodbref=None,
                include_accessioned=False):
    """
    Returns a `graflipy.ega.schema_1_5_0.AnalysisSet` instance representing an
    `ANALYSIS_SET` containing `ANALYSIS/ANALYSIS_TYPE/REFERENCE_ALIGNMENT`
    elements

    Args:
        paths: list of paths to bams on a locally accessible filesystem
        md5dir: directory containing the .bam.md5 and .bam.gpg.md5 files for
            all bams in `paths`
        egastudy: EGA accession of the study the bam belongs to
        egadir: directory in the EGA upload box that contains/will contain
            the encrypted bam
        nodbref: Optional[ReferenceAssembly]. If this is supplied then the
            database is not queried for any metadata. A warning is logged and
            empty string '' is used for all corresponding properties. The
            resulting XML won't validate at EGA - it does not have any info
            about the parent sample of analsis elements, for a start - but
            this can be useful for building scaffold XML files to be manually
            completed
        include_accessioned:
            include ANALYSIS elements where the corresponding file already has
            an `:egaAccession` value recorded in the database (default=False)

    Raises:
        MetadataConstructionError containing accumulated metadata construction
            errors from all the analyses
    """
    md5dir = Path(md5dir)
    paths = [Path(path) for path in paths]
    analyses, errors = [], []
    for path in paths:
        bam = path.name
        bamgpg = bam + '.gpg'
        try:
            analyses.append(
                analysis_refalign(
                    path,
                    get_md5(md5dir.joinpath(f'{bam}.md5'), bam),
                    get_md5(md5dir.joinpath(f'{bamgpg}.md5'), bamgpg),
                    egastudy,
                    egadir,
                    nodbref))
        except (MetadataConstructionError, FileNotFoundError) as mcerr:
            errors.append(mcerr)
    if errors:
        raise MetadataConstructionError('\n'.join(str(err) for err in errors))

    include = filter(
        lambda a: include_accessioned or not a.accession, analyses)

    return AnalysisSet(analysis=list(include))


def dataset_analysisref(
        alias, title, description, analysis_accessions,
        policy_accession=None, is_icgc=False, links=None):
    """
    Returns `graflipy.ega.schema_1_5_0.DatasetType` instance representing a
    `DATASET` containing `ANALYSIS_REF` elements

    Args:
        alias: alias for the dataset
        title: title for the dataset
        description: description for the dataset
        analysis_accessions: list of EGAZ accession strings
        policy_accession: EGAP accession string - required iff `is_icgc=False`
        is_icgc: use ICGC policy accession & links (default=False)
        links: list of (label, URL) tuples
    """
    LOGGER.info('building metadata for dataset %s', alias)

    links = links or []
    if is_icgc != (policy_accession is None):
        raise ValueError(ERR_DATASET_POLICY)

    if is_icgc:
        links.append(('ICGC Data Portal', 'http://dcc.icgc.org'))
        policy_accession = CONF.ega.icgcDataPolicyAccession

    return DatasetType(
        alias=alias,
        title=title,
        description=description,
        analysis_ref=[
            DatasetType.AnalysisRef(
                accession=accession
            ) for accession in analysis_accessions
        ],
        policy_ref=DatasetType.PolicyRef(
            accession=policy_accession
        ),
        dataset_links=DatasetType.DatasetLinks(
            dataset_link=[
                LinkType(
                    url_link=LinkType.UrlLink(
                        label=label,
                        url=url
                    )
                ) for (label, url) in links
            ]
        )
    )


def datasets(dss):
    """
    Returns `graflipy.ega.schema_1_5_0.Datasets` instance representing a
    `DATASETS` containing `DATASET` elements

    Args:
        dss: list of DatasetType instances
    """
    return Datasets(dataset=dss)


def sample(uuid):
    """
    Returns a `graflipy.ega.schema_1_5_0.SampleType` instance representing a
    `SAMPLE` element

    Args:
        uuid: UUID string of the associated `:CollectedSample` in the db

    Raises:
        MetadataConstructionError if the specified sample is not found in the
            datbase, multiple matches are found, or the sample metadata is
            incomplete.
    """
    LOGGER.info('building metadata for collectedsample:%s', uuid)

    dbmeta = dbmeta_sample(uuid)

    return SampleType(
        alias=uuid,
        accession=dbmeta.ega_accession,
        sample_name=SampleType.SampleName(
            taxon_id=dbmeta.reference_species.taxon_id,
            scientific_name=dbmeta.reference_species.scientific_name,
            common_name=dbmeta.reference_species.common_name
        ),
        description=dbmeta.sample_material,
        sample_attributes=SampleType.SampleAttributes(
            sample_attribute=[
                AttributeType(tag='Sample ID',
                              value=dbmeta.sample_publication_id),
                AttributeType(tag='Donor ID',
                              value=dbmeta.donor_publication_id),
                AttributeType(tag='Phenotype', value=dbmeta.phenotype),
                AttributeType(tag='subject_id', value=dbmeta.donor_uuid),
                AttributeType(tag='gender', value=dbmeta.donor_sex),
            ]
        )
    )


def sampleset(uuids, include_accessioned=False):
    """
    Returns a `graflipy.ega.schema_1_5_0.SampleSet` instance representing a
    `SAMPLE_SET` containing `SAMPLE` elements

    Args:
        uuids: list of UUID strings of `:CollectedSample` instances
        include_accessioned:
            include SAMPLE elements where the corresponding file already has
            an `:egaAccession` value recorded in the database (default=False)

    Raises:
        MetadataConstructionError containing accumulated metadata construction
            errors from all the samples
    """
    samples, errors = [], []
    for uuid in uuids:
        try:
            samples.append(sample(uuid))
        except MetadataConstructionError as mcerr:
            errors.append(mcerr)
    if errors:
        raise MetadataConstructionError('; '.join(str(err) for err in errors))

    include = filter(lambda s: include_accessioned or not s.accession, samples)

    return SampleSet(sample=list(include))


def submission(alias, actions):
    """
    Returns a `graflipy.ega.schema_1_5_0.SubmissionType` instance representing
    a `SUBMISSION`

    Args:
        alias: alias for the submission
        actions: list of `SubmissionType.Actions.Action`
    """
    return SubmissionType(
        alias=alias,
        broker_name='EGA',
        center_name=CONF.ega.centerName,
        lab_name=CONF.ega.labName,
        contacts=SubmissionType.Contacts(
            contact=[
                SubmissionType.Contacts.Contact(
                    name=contact.name,
                    inform_on_error=contact.email,
                    inform_on_status=contact.email
                ) for contact in CONF.ega.contacts
            ]
        ),
        actions=SubmissionType.Actions(
            action=actions
        )
    )


def submissionset(submissions):
    """
    Returns `graflipy.ega.schema_1_5_0.SubmissionSet` instance representing a
    `SUBMISSION_SET` containing `SUBMISSION` elements

    Args:
        submissions: list of SubmissionType instances
    """
    return SubmissionSet(submission=submissions)
