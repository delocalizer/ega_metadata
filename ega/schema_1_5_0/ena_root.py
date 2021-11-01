from dataclasses import dataclass, field
from typing import List, Optional
from graflipy.ega.schema_1_5_0.ena_embl import EntryType
from graflipy.ega.schema_1_5_0.ena_project import (
    ProjectSetType,
    ProjectType,
)
from graflipy.ega.schema_1_5_0.ena_taxonomy import TaxonType
from graflipy.ega.schema_1_5_0.sra_analysis import (
    AnalysisSetType,
    AnalysisType,
)
from graflipy.ega.schema_1_5_0.sra_experiment import (
    ExperimentSetType,
    ExperimentType,
)
from graflipy.ega.schema_1_5_0.sra_run import (
    RunSetType,
    RunType,
)
from graflipy.ega.schema_1_5_0.sra_sample import (
    SampleSetType,
    SampleType,
)
from graflipy.ega.schema_1_5_0.sra_study import (
    StudySetType,
    StudyType,
)
from graflipy.ega.schema_1_5_0.sra_submission import (
    SubmissionSetType,
    SubmissionType,
)


@dataclass
class EntrySetType:
    entry: List[EntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class TaxonSetType:
    taxon: List[TaxonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class RootType:
    """
    A container for any combination of ENA objects.
    """
    analysis_set: List[AnalysisSetType] = field(
        default_factory=list,
        metadata={
            "name": "ANALYSIS_SET",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    analysis: List[AnalysisType] = field(
        default_factory=list,
        metadata={
            "name": "ANALYSIS",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    experiment_set: List[ExperimentSetType] = field(
        default_factory=list,
        metadata={
            "name": "EXPERIMENT_SET",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    experiment: List[ExperimentType] = field(
        default_factory=list,
        metadata={
            "name": "EXPERIMENT",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    run_set: List[RunSetType] = field(
        default_factory=list,
        metadata={
            "name": "RUN_SET",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    run: List[RunType] = field(
        default_factory=list,
        metadata={
            "name": "RUN",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    study_set: List[StudySetType] = field(
        default_factory=list,
        metadata={
            "name": "STUDY_SET",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    study: List[StudyType] = field(
        default_factory=list,
        metadata={
            "name": "STUDY",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    sample_set: List[SampleSetType] = field(
        default_factory=list,
        metadata={
            "name": "SAMPLE_SET",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    sample: List[SampleType] = field(
        default_factory=list,
        metadata={
            "name": "SAMPLE",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    submission_set: List[SubmissionSetType] = field(
        default_factory=list,
        metadata={
            "name": "SUBMISSION_SET",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    submission: List[SubmissionType] = field(
        default_factory=list,
        metadata={
            "name": "SUBMISSION",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    entry_set: List[EntrySetType] = field(
        default_factory=list,
        metadata={
            "name": "entrySet",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    entry: List[EntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    taxon_set: List[TaxonSetType] = field(
        default_factory=list,
        metadata={
            "name": "taxonSet",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    taxon: List[TaxonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    project_set: List[ProjectSetType] = field(
        default_factory=list,
        metadata={
            "name": "PROJECT_SET",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    project: List[ProjectType] = field(
        default_factory=list,
        metadata={
            "name": "PROJECT",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    request: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "ROOT"
