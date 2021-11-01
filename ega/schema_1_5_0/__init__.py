from graflipy.ega.schema_1_5_0.ega_dac import (
    Dac,
    DacSet,
    DacSetType,
    DacType,
)
from graflipy.ega.schema_1_5_0.ega_dataset import (
    Dataset,
    Datasets,
    DatasetType,
    DatasetTypeDatasetType,
    DatasetsType,
)
from graflipy.ega.schema_1_5_0.ega_policy import (
    Policy,
    PolicySet,
    PolicySetType,
    PolicyType,
)
from graflipy.ega.schema_1_5_0.ena_assembly import (
    Assembly,
    AssemblySet,
    AssemblySetType,
    AssemblyType,
    AssemblyTypeAssemblyLevel,
    AssemblyTypeGenomeRepresentation,
    ChromosomeType,
)
from graflipy.ega.schema_1_5_0.ena_checklist import (
    Checklist,
    ChecklistSet,
    ChecklistSetType,
    ChecklistType,
    ChecklistTypeChecklistType,
    FieldGroupRestrictionType,
    FieldMandatory,
    FieldMultiplicity,
    TaxonFieldRestrictionType,
)
from graflipy.ega.schema_1_5_0.ena_embl import (
    EntryType,
    EntryTypeTopology,
    XrefType,
    Entry,
    EntrySet,
    ReferenceType,
)
from graflipy.ega.schema_1_5_0.ena_project import (
    OrganismType,
    Project,
    ProjectSet,
    ProjectSetType,
    ProjectType,
    PublicationType,
)
from graflipy.ega.schema_1_5_0.ena_root import (
    EntrySetType,
    Root,
    RootType,
    TaxonSetType,
)
from graflipy.ega.schema_1_5_0.ena_sample_group import (
    SampleGroup,
    SampleGroupSet,
    SampleGroupSetType,
    SampleGroupType,
)
from graflipy.ega.schema_1_5_0.ena_taxonomy import (
    ChildTaxonType,
    ParentTaxonType,
    TaxonType,
    SynonymType,
    Taxon,
    TaxonSet,
)
from graflipy.ega.schema_1_5_0.sra_analysis import (
    Analysis,
    AnalysisSet,
    AnalysisFileType,
    AnalysisFileTypeChecksumMethod,
    AnalysisFileTypeFiletype,
    AnalysisSetType,
    AnalysisType,
    GenomeMapPlatform,
    SequenceAssemblyMolType,
    SequenceVariationExperimentType,
)
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    BasecallMatchEdge,
    IdentifierType,
    LinkType,
    NameType,
    PipelineType,
    PlatformType,
    ProcessingType,
    QualifiedNameType,
    ReadSpecReadClass,
    ReadSpecReadType,
    ReferenceAssemblyType,
    ReferenceSequenceType,
    SequencingDirectivesType,
    SequencingDirectivesTypeSampleDemuxDirective,
    SpotDescriptorType,
    Urltype,
    XrefType,
    Type454Model,
    TypeAbiSolidModel,
    TypeCgmodel,
    TypeCapillaryModel,
    TypeHelicosModel,
    TypeIlluminaModel,
    TypeIontorrentModel,
    TypeOxfordNanoporeModel,
    TypePacBioModel,
)
from graflipy.ega.schema_1_5_0.sra_experiment import (
    Experiment,
    ExperimentSet,
    ExperimentSetType,
    ExperimentType,
    LocusLocusName,
    LibraryDescriptorType,
    LibraryType,
    PoolMemberType,
    SampleDescriptorType,
    TypeLibrarySelection,
    TypeLibrarySource,
    TypeLibraryStrategy,
)
from graflipy.ega.schema_1_5_0.sra_receipt import (
    ExtIdType,
    Id,
    IdStatus,
    Receipt,
    ReceiptActions,
)
from graflipy.ega.schema_1_5_0.sra_run import (
    FileAsciiOffset,
    FileChecksumMethod,
    FileFiletype,
    FileQualityEncoding,
    FileQualityScoringSystem,
    Run,
    RunSet,
    RunSetType,
    RunType,
)
from graflipy.ega.schema_1_5_0.sra_sample import (
    Sample,
    SampleSet,
    SampleSetType,
    SampleType,
)
from graflipy.ega.schema_1_5_0.sra_study import (
    Study,
    StudySet,
    StudyTypeExistingStudyType,
    StudySetType,
    StudyType,
)
from graflipy.ega.schema_1_5_0.sra_submission import (
    AddSchema,
    ModifySchema,
    Submission,
    SubmissionSet,
    SubmissionSetType,
    SubmissionType,
    ValidateSchema,
)

# below here added manually

XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ANALYSISXSD = 'ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.analysis.xsd'
DATASETXSD = 'ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/EGA.dataset.xsd'
SAMPLEXSD = 'ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.sample.xsd'
SUBMISSIONXSD = 'ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/SRA.submission.xsd'
