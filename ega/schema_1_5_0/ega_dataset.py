from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    IdentifierType,
    LinkType,
)


class DatasetTypeDatasetType(Enum):
    WHOLE_GENOME_SEQUENCING = "Whole genome sequencing"
    EXOME_SEQUENCING = "Exome sequencing"
    GENOTYPING_BY_ARRAY = "Genotyping by array"
    TRANSCRIPTOME_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = "Transcriptome profiling by high-throughput sequencing"
    TRANSCRIPTOME_PROFILING_BY_ARRAY = "Transcriptome profiling by array"
    AMPLICON_SEQUENCING = "Amplicon sequencing"
    METHYLATION_BINDING_DOMAIN_SEQUENCING = "Methylation binding domain sequencing"
    METHYLATION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = "Methylation profiling by high-throughput sequencing"
    PHENOTYPE_INFORMATION = "Phenotype information"
    STUDY_SUMMARY_INFORMATION = "Study summary information"
    GENOMIC_VARIANT_CALLING = "Genomic variant calling"
    CHROMATIN_ACCESSIBILITY_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = "Chromatin accessibility profiling by high-throughput sequencing"
    HISTONE_MODIFICATION_PROFILING_BY_HIGH_THROUGHPUT_SEQUENCING = "Histone modification profiling by high-throughput sequencing"
    CHIP_SEQ = "Chip-Seq"


@dataclass
class DatasetType:
    """
    Describes an object that contains the samples in the data set.

    :ivar identifiers:
    :ivar title: Short text that can be used to call out data sets in
        searches or in displays.
    :ivar description: Free-form text describing the data sets.
    :ivar dataset_type:
    :ivar run_ref: The RUN_REF descriptor identifies the runs which are
        part of this dataset.
    :ivar analysis_ref: The ANALYSIS_REF descriptor identifies the
        analyses which are part of this dataset.
    :ivar policy_ref: The POLICY_REF identifies the data access policy
        controlling this data set.
    :ivar dataset_links: Links to related resources.
    :ivar dataset_attributes: Properties and attributes of the data set.
        These can be entered as free-form tag-value pairs. Submitters
        may be asked to follow a community established ontology when
        describing the work.
    :ivar alias: Submitter designated name of the SRA document of this
        type.  At minimum alias should be unique throughout the
        submission of this document type.  If center_name is specified,
        the name should be unique in all submissions from that center of
        this document type.
    :ivar center_name: Owner authority of this document and namespace
        for submitter's name of this document.  If not provided, then
        the submitter is regarded as "Individual" and document
        resolution can only happen within the submission.
    :ivar broker_name: Broker authority of this document.  If not
        provided, then the broker is considered "direct".
    :ivar accession: The document's accession as assigned by the Home
        Archive.
    """
    identifiers: Optional[IdentifierType] = field(
        default=None,
        metadata={
            "name": "IDENTIFIERS",
            "type": "Element",
            "namespace": "",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "TITLE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "DESCRIPTION",
            "type": "Element",
            "namespace": "",
        }
    )
    dataset_type: List[DatasetTypeDatasetType] = field(
        default_factory=list,
        metadata={
            "name": "DATASET_TYPE",
            "type": "Element",
            "namespace": "",
        }
    )
    run_ref: List["DatasetType.RunRef"] = field(
        default_factory=list,
        metadata={
            "name": "RUN_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    analysis_ref: List["DatasetType.AnalysisRef"] = field(
        default_factory=list,
        metadata={
            "name": "ANALYSIS_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    policy_ref: Optional["DatasetType.PolicyRef"] = field(
        default=None,
        metadata={
            "name": "POLICY_REF",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dataset_links: Optional["DatasetType.DatasetLinks"] = field(
        default=None,
        metadata={
            "name": "DATASET_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )
    dataset_attributes: Optional["DatasetType.DatasetAttributes"] = field(
        default=None,
        metadata={
            "name": "DATASET_ATTRIBUTES",
            "type": "Element",
            "namespace": "",
        }
    )
    alias: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    center_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    broker_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    accession: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class RunRef:
        """
        :ivar identifiers:
        :ivar refname: Identifies a record by name that is known within
            the namespace defined by attribute "refcenter" Use this
            field when referencing an object for which an accession has
            not yet been issued.
        :ivar refcenter: The center namespace of the attribute
            "refname". When absent, the namespace is assumed to be the
            current submission.
        :ivar accession: Identifies a record by its accession.  The
            scope of resolution is the entire Archive.
        """
        identifiers: Optional[IdentifierType] = field(
            default=None,
            metadata={
                "name": "IDENTIFIERS",
                "type": "Element",
                "namespace": "",
            }
        )
        refname: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        refcenter: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        accession: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class AnalysisRef:
        """
        :ivar identifiers:
        :ivar refname: Identifies a record by name that is known within
            the namespace defined by attribute "refcenter" Use this
            field when referencing an object for which an accession has
            not yet been issued.
        :ivar refcenter: The center namespace of the attribute
            "refname". When absent, the namespace is assumed to be the
            current submission.
        :ivar accession: Identifies a record by its accession.  The
            scope of resolution is the entire Archive.
        """
        identifiers: Optional[IdentifierType] = field(
            default=None,
            metadata={
                "name": "IDENTIFIERS",
                "type": "Element",
                "namespace": "",
            }
        )
        refname: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        refcenter: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        accession: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class PolicyRef:
        """
        :ivar identifiers:
        :ivar refname: Identifies a record by name that is known within
            the namespace defined by attribute "refcenter" Use this
            field when referencing an object for which an accession has
            not yet been issued.
        :ivar refcenter: The center namespace of the attribute
            "refname". When absent, the namespace is assumed to be the
            current submission.
        :ivar accession: Identifies a record by its accession.  The
            scope of resolution is the entire Archive.
        """
        identifiers: Optional[IdentifierType] = field(
            default=None,
            metadata={
                "name": "IDENTIFIERS",
                "type": "Element",
                "namespace": "",
            }
        )
        refname: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        refcenter: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        accession: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class DatasetLinks:
        dataset_link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "name": "DATASET_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class DatasetAttributes:
        dataset_attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "name": "DATASET_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class Dataset(DatasetType):
    class Meta:
        name = "DATASET"


@dataclass
class DatasetsType:
    dataset: List[Dataset] = field(
        default_factory=list,
        metadata={
            "name": "DATASET",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Datasets(DatasetsType):
    """
    Container for a set of data sets.
    """
    class Meta:
        name = "DATASETS"
