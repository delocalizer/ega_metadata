from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    IdentifierType,
    LinkType,
)


class AssemblyTypeAssemblyLevel(Enum):
    COMPLETE_GENOME = "complete genome"
    CHROMOSOME = "chromosome"
    SCAFFOLD = "scaffold"
    CONTIG = "contig"


class AssemblyTypeGenomeRepresentation(Enum):
    FULL = "full"
    PARTIAL = "partial"


class ChromosomeType(Enum):
    PLASTID = "Plastid"
    KINETOPLAST = "Kinetoplast"
    SEGMENT = "Segment"
    APICOPLAST = "Apicoplast"
    VIRUS = "Virus"
    MITOCHONDRIAL_MISCELLANEOUS = "Mitochondrial Miscellaneous"
    PLASMID = "Plasmid"
    NUCLEOMORPH = "Nucleomorph"
    MACRONUCLEUS = "Macronucleus"
    CHLOROPLAST = "Chloroplast"
    MITOCHONDRION = "Mitochondrion"
    VIRUS_CHROMOSOME = "Virus Chromosome"
    EXTRACHROMOSOMAL_ELEMENT = "Extrachromosomal Element"
    MISCELLANEOUS = "Miscellaneous"
    PROVIRUS = "Provirus"
    CHROMOSOME = "Chromosome"
    NON_NUCLEAR_MISCELLANEOUS = "Non-nuclear Miscellaneous"
    CHROMATOPHORE = "Chromatophore"
    PROVIRUS_CHROMOSOME = "Provirus Chromosome"
    MITOCHONDRIAL_PLASMID = "Mitochondrial Plasmid"
    LINKAGE_GROUP = "Linkage Group"
    CYANELLE = "Cyanelle"


@dataclass
class AssemblyType:
    """
    :ivar identifiers:
    :ivar title:
    :ivar description:
    :ivar name:
    :ivar assembly_level:
    :ivar genome_representation:
    :ivar taxon:
    :ivar sample_ref:
    :ivar study_ref:
    :ivar wgs_set:
    :ivar chromosomes:
    :ivar assembly_links:
    :ivar assembly_attributes:
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAME",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    assembly_level: Optional[AssemblyTypeAssemblyLevel] = field(
        default=None,
        metadata={
            "name": "ASSEMBLY_LEVEL",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    genome_representation: Optional[AssemblyTypeGenomeRepresentation] = field(
        default=None,
        metadata={
            "name": "GENOME_REPRESENTATION",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    taxon: Optional["AssemblyType.Taxon"] = field(
        default=None,
        metadata={
            "name": "TAXON",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    sample_ref: Optional["AssemblyType.SampleRef"] = field(
        default=None,
        metadata={
            "name": "SAMPLE_REF",
            "type": "Element",
            "namespace": "",
        }
    )
    study_ref: Optional["AssemblyType.StudyRef"] = field(
        default=None,
        metadata={
            "name": "STUDY_REF",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    wgs_set: List["AssemblyType.WgsSet"] = field(
        default_factory=list,
        metadata={
            "name": "WGS_SET",
            "type": "Element",
            "namespace": "",
        }
    )
    chromosomes: Optional["AssemblyType.Chromosomes"] = field(
        default=None,
        metadata={
            "name": "CHROMOSOMES",
            "type": "Element",
            "namespace": "",
        }
    )
    assembly_links: Optional["AssemblyType.AssemblyLinks"] = field(
        default=None,
        metadata={
            "name": "ASSEMBLY_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )
    assembly_attributes: Optional["AssemblyType.AssemblyAttributes"] = field(
        default=None,
        metadata={
            "name": "ASSEMBLY_ATTRIBUTES",
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
    class Taxon:
        taxon_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "TAXON_ID",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        scientific_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "SCIENTIFIC_NAME",
                "type": "Element",
                "namespace": "",
            }
        )
        common_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "COMMON_NAME",
                "type": "Element",
                "namespace": "",
            }
        )
        strain: Optional[str] = field(
            default=None,
            metadata={
                "name": "STRAIN",
                "type": "Element",
                "namespace": "",
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
    class WgsSet:
        prefix: Optional[str] = field(
            default=None,
            metadata={
                "name": "PREFIX",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        version: Optional[int] = field(
            default=None,
            metadata={
                "name": "VERSION",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )

    @dataclass
    class Chromosomes:
        chromosome: List["AssemblyType.Chromosomes.Chromosome"] = field(
            default_factory=list,
            metadata={
                "name": "CHROMOSOME",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Chromosome:
            name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NAME",
                    "type": "Element",
                    "namespace": "",
                }
            )
            type: Optional[ChromosomeType] = field(
                default=None,
                metadata={
                    "name": "TYPE",
                    "type": "Element",
                    "namespace": "",
                }
            )
            accession: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class AssemblyLinks:
        assembly_link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "name": "ASSEMBLY_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class AssemblyAttributes:
        assembly_attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "name": "ASSEMBLY_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class Assembly(AssemblyType):
    class Meta:
        name = "ASSEMBLY"


@dataclass
class AssemblySetType:
    assembly: List[Assembly] = field(
        default_factory=list,
        metadata={
            "name": "ASSEMBLY",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AssemblySet(AssemblySetType):
    """
    A container of assembly objects.
    """
    class Meta:
        name = "ASSEMBLY_SET"
