from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    IdentifierType,
    LinkType,
    ReferenceSequenceType,
)


class AnalysisFileTypeChecksumMethod(Enum):
    """
    :cvar MD5: Checksum generated by the MD5 method (md5sum in
        unix).
    """
    MD5 = "MD5"


class AnalysisFileTypeFiletype(Enum):
    """
    :cvar TAB: A tab delimited text file that can be viewed as a
        spreadsheet. The first line should contain column headers.
    :cvar BAM: Binary form of the Sequence alignment/map format
        for read placements, from the SAM tools project. See
        http://sourceforge.net/projects/samtools/
    :cvar BAI: Index sorted alignment for fast random  access.See
        http://sourceforge.net/projects/samtools/
    :cvar CRAM:
    :cvar VCF:
    :cvar VCF_AGGREGATE:
    :cvar BCF:
    :cvar TABIX:
    :cvar WIG:
    :cvar BED:
    :cvar GFF:
    :cvar FASTA:
    :cvar FASTQ:
    :cvar CONTIG_FASTA:
    :cvar CONTIG_FLATFILE:
    :cvar SCAFFOLD_FASTA:
    :cvar SCAFFOLD_FLATFILE:
    :cvar SCAFFOLD_AGP:
    :cvar CHROMOSOME_FASTA:
    :cvar CHROMOSOME_FLATFILE:
    :cvar CHROMOSOME_AGP:
    :cvar CHROMOSOME_LIST:
    :cvar UNLOCALISED_CONTIG_LIST:
    :cvar UNLOCALISED_SCAFFOLD_LIST:
    :cvar SAMPLE_LIST:
    :cvar README_FILE:
    :cvar PHENOTYPE_FILE:
    :cvar BNX:
    :cvar CMAP:
    :cvar VIS_CMAP:
    :cvar VIS_XMAP:
    :cvar OTHER:
    """
    TAB = "tab"
    BAM = "bam"
    BAI = "bai"
    CRAM = "cram"
    VCF = "vcf"
    VCF_AGGREGATE = "vcf_aggregate"
    BCF = "bcf"
    TABIX = "tabix"
    WIG = "wig"
    BED = "bed"
    GFF = "gff"
    FASTA = "fasta"
    FASTQ = "fastq"
    CONTIG_FASTA = "contig_fasta"
    CONTIG_FLATFILE = "contig_flatfile"
    SCAFFOLD_FASTA = "scaffold_fasta"
    SCAFFOLD_FLATFILE = "scaffold_flatfile"
    SCAFFOLD_AGP = "scaffold_agp"
    CHROMOSOME_FASTA = "chromosome_fasta"
    CHROMOSOME_FLATFILE = "chromosome_flatfile"
    CHROMOSOME_AGP = "chromosome_agp"
    CHROMOSOME_LIST = "chromosome_list"
    UNLOCALISED_CONTIG_LIST = "unlocalised_contig_list"
    UNLOCALISED_SCAFFOLD_LIST = "unlocalised_scaffold_list"
    SAMPLE_LIST = "sample_list"
    README_FILE = "readme_file"
    PHENOTYPE_FILE = "phenotype_file"
    BNX = "bnx"
    CMAP = "cmap"
    VIS_CMAP = "vis_cmap"
    VIS_XMAP = "vis_xmap"
    OTHER = "other"


class GenomeMapPlatform(Enum):
    BIO_NANO = "BioNano"


class SequenceAssemblyMolType(Enum):
    GENOMIC_DNA = "genomic DNA"
    GENOMIC_RNA = "genomic RNA"
    VIRAL_C_RNA = "viral cRNA"


class SequenceVariationExperimentType(Enum):
    WHOLE_GENOME_SEQUENCING = "Whole genome sequencing"
    EXOME_SEQUENCING = "Exome sequencing"
    GENOTYPING_BY_ARRAY = "Genotyping by array"
    TRANSCRIPTOMICS = "transcriptomics"
    CURATION = "Curation"


@dataclass
class AnalysisFileType:
    """
    :ivar filename: The file name.
    :ivar filetype: The type of the file.
    :ivar checksum_method: The checksum method.
    :ivar checksum: The file checksum.
    :ivar unencrypted_checksum: The checksum of the unencrypted file
        (used in conjunction with the checksum of an encrypted file).
    :ivar checklist: The name of the checklist.
    """
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    filetype: Optional[AnalysisFileTypeFiletype] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    checksum_method: Optional[AnalysisFileTypeChecksumMethod] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    checksum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    unencrypted_checksum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    checklist: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AnalysisType:
    """
    A SRA analysis object captures sequence analysis results including sequence
    alignments, sequence variations and sequence annotations.

    :ivar identifiers:
    :ivar title: Title of the analyis object which will be displayed in
        database search results.
    :ivar description: Describes the analysis in detail.
    :ivar study_ref: Establishes a relationship between the analysis and
        the                         parent study.
    :ivar sample_ref: One of more samples associated with the
        analysis.
    :ivar experiment_ref:
    :ivar run_ref: One or more runs associated with the
        analysis.
    :ivar analysis_ref: One or more runs associated with the
        analysis.
    :ivar analysis_type: The type of the analysis.
    :ivar files: Files associated with the
        analysis.
    :ivar analysis_links: Links to resources related to this analysis.
    :ivar analysis_attributes: Properties and attributes of an analysis.
        These can be                         entered as free-form tag-
        value pairs.
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
    :ivar analysis_center: If applicable, the center name of the
        institution responsible                     for this analysis.
    :ivar analysis_date: The date when this analysis was produced.
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
            "required": True,
        }
    )
    study_ref: Optional["AnalysisType.StudyRef"] = field(
        default=None,
        metadata={
            "name": "STUDY_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    sample_ref: List["AnalysisType.SampleRef"] = field(
        default_factory=list,
        metadata={
            "name": "SAMPLE_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    experiment_ref: List["AnalysisType.ExperimentRef"] = field(
        default_factory=list,
        metadata={
            "name": "EXPERIMENT_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    run_ref: List["AnalysisType.RunRef"] = field(
        default_factory=list,
        metadata={
            "name": "RUN_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    analysis_ref: List["AnalysisType.AnalysisRef"] = field(
        default_factory=list,
        metadata={
            "name": "ANALYSIS_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    analysis_type: Optional["AnalysisType.AnalysisType"] = field(
        default=None,
        metadata={
            "name": "ANALYSIS_TYPE",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    files: Optional["AnalysisType.Files"] = field(
        default=None,
        metadata={
            "name": "FILES",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    analysis_links: Optional["AnalysisType.AnalysisLinks"] = field(
        default=None,
        metadata={
            "name": "ANALYSIS_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )
    analysis_attributes: Optional["AnalysisType.AnalysisAttributes"] = field(
        default=None,
        metadata={
            "name": "ANALYSIS_ATTRIBUTES",
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
    analysis_center: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    analysis_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class StudyRef:
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
    class SampleRef:
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
        :ivar label: A label associating the sample with BAM (@RG/ID or
            @RG/SM) or VCF file samples.
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
        label: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class ExperimentRef:
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
        :ivar label: A label associating the run with BAM (@RG/ID).
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
        label: Optional[str] = field(
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
        :ivar label: A label associating the run with BAM (@RG/ID).
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
        label: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class AnalysisType:
        reference_alignment: Optional[ReferenceSequenceType] = field(
            default=None,
            metadata={
                "name": "REFERENCE_ALIGNMENT",
                "type": "Element",
                "namespace": "",
            }
        )
        sequence_variation: Optional["AnalysisType.AnalysisType.SequenceVariation"] = field(
            default=None,
            metadata={
                "name": "SEQUENCE_VARIATION",
                "type": "Element",
                "namespace": "",
            }
        )
        sequence_assembly: Optional["AnalysisType.AnalysisType.SequenceAssembly"] = field(
            default=None,
            metadata={
                "name": "SEQUENCE_ASSEMBLY",
                "type": "Element",
                "namespace": "",
            }
        )
        sequence_annotation: Optional["AnalysisType.AnalysisType.SequenceAnnotation"] = field(
            default=None,
            metadata={
                "name": "SEQUENCE_ANNOTATION",
                "type": "Element",
                "namespace": "",
            }
        )
        reference_sequence: Optional[object] = field(
            default=None,
            metadata={
                "name": "REFERENCE_SEQUENCE",
                "type": "Element",
                "namespace": "",
            }
        )
        sample_phenotype: Optional["AnalysisType.AnalysisType.SamplePhenotype"] = field(
            default=None,
            metadata={
                "name": "SAMPLE_PHENOTYPE",
                "type": "Element",
                "namespace": "",
            }
        )
        processed_reads: Optional[object] = field(
            default=None,
            metadata={
                "name": "PROCESSED_READS",
                "type": "Element",
                "namespace": "",
            }
        )
        genome_map: Optional["AnalysisType.AnalysisType.GenomeMap"] = field(
            default=None,
            metadata={
                "name": "GENOME_MAP",
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class SequenceVariation(ReferenceSequenceType):
            experiment_type: List[SequenceVariationExperimentType] = field(
                default_factory=list,
                metadata={
                    "name": "EXPERIMENT_TYPE",
                    "type": "Element",
                    "namespace": "",
                }
            )
            program: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PROGRAM",
                    "type": "Element",
                    "namespace": "",
                }
            )
            platform: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PLATFORM",
                    "type": "Element",
                    "namespace": "",
                }
            )
            imputation: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "IMPUTATION",
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class SequenceAssembly:
            name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NAME",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            partial: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "PARTIAL",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            coverage: Optional[str] = field(
                default=None,
                metadata={
                    "name": "COVERAGE",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            program: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PROGRAM",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            platform: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PLATFORM",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            min_gap_length: Optional[int] = field(
                default=None,
                metadata={
                    "name": "MIN_GAP_LENGTH",
                    "type": "Element",
                    "namespace": "",
                }
            )
            mol_type: Optional[SequenceAssemblyMolType] = field(
                default=None,
                metadata={
                    "name": "MOL_TYPE",
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class SequenceAnnotation:
            pass

        @dataclass
        class SamplePhenotype:
            pass

        @dataclass
        class GenomeMap:
            program: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PROGRAM",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            platform: Optional[GenomeMapPlatform] = field(
                default=None,
                metadata={
                    "name": "PLATFORM",
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

    @dataclass
    class AnalysisLinks:
        analysis_link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "name": "ANALYSIS_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class AnalysisAttributes:
        analysis_attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "name": "ANALYSIS_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Files:
        file: List[AnalysisFileType] = field(
            default_factory=list,
            metadata={
                "name": "FILE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class Analysis(AnalysisType):
    class Meta:
        name = "ANALYSIS"


@dataclass
class AnalysisSetType:
    analysis: List[AnalysisType] = field(
        default_factory=list,
        metadata={
            "name": "ANALYSIS",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class AnalysisSet(AnalysisSetType):
    """
    A container of analysis objects.
    """
    class Meta:
        name = "ANALYSIS_SET"