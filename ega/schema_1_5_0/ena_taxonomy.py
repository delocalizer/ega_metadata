from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class ChildTaxonType:
    children: Optional["ChildTaxonType.Children"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    scientific_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "scientificName",
            "type": "Attribute",
            "required": True,
        }
    )
    common_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "commonName",
            "type": "Attribute",
        }
    )
    tax_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "taxId",
            "type": "Attribute",
            "required": True,
        }
    )
    rank: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Children:
        taxon: List["ChildTaxonType"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )


class SynonymType(Enum):
    SYNONYM = "synonym"
    COMMON_NAME = "common name"
    ACRONYM = "acronym"
    ANAMORPH = "anamorph"
    TELEOMORPH = "teleomorph"
    EQUIVALENT_NAME = "equivalent name"
    INCLUDES = "includes"
    IS_PART = "is-part"


@dataclass
class ParentTaxonType:
    """
    :ivar children: A list of child taxons.
    :ivar scientific_name: The scientific name for the taxon.
    :ivar common_name: The preferred common name for the taxon.
    :ivar tax_id: The taxon identifier.
    :ivar rank: The taxonomic rank.
    :ivar hidden: If true then the taxon is intended to be hidden from
        the abbreviated lineage.
    """
    children: Optional["ParentTaxonType.Children"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    scientific_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "scientificName",
            "type": "Attribute",
            "required": True,
        }
    )
    common_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "commonName",
            "type": "Attribute",
        }
    )
    tax_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "taxId",
            "type": "Attribute",
            "required": True,
        }
    )
    rank: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Children:
        taxon: List[ChildTaxonType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )


@dataclass
class TaxonType:
    """
    :ivar lineage: The taxonomic lineage.
    :ivar children: A list of child taxons.
    :ivar synonym: A list of other names for the taxon.
    :ivar scientific_name: The scientific name for the taxon.
    :ivar common_name: The preferred common name for the taxon.
    :ivar tax_id: The taxon identifier.
    :ivar parent_tax_id: The taxonomy identifier for the parent taxon.
    :ivar rank: The taxonomic rank.
    :ivar hidden: If true then the taxon is intended to be hidden from
        the abbreviated lineage.
    :ivar taxonomic_division: The taxonomic division.
    :ivar genetic_code: The translation table for protein coding
        sequences.
    :ivar mitochondrial_genetic_code: The translation table for
        mitochondrial protein coding sequences.
    """
    lineage: Optional["TaxonType.Lineage"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    children: Optional["TaxonType.Children"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    synonym: List["TaxonType.Synonym"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    scientific_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "scientificName",
            "type": "Attribute",
            "required": True,
        }
    )
    common_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "commonName",
            "type": "Attribute",
        }
    )
    tax_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "taxId",
            "type": "Attribute",
            "required": True,
        }
    )
    parent_tax_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "parentTaxId",
            "type": "Attribute",
        }
    )
    rank: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    taxonomic_division: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonomicDivision",
            "type": "Attribute",
            "required": True,
        }
    )
    genetic_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "geneticCode",
            "type": "Attribute",
        }
    )
    mitochondrial_genetic_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "mitochondrialGeneticCode",
            "type": "Attribute",
        }
    )

    @dataclass
    class Lineage:
        taxon: List[ParentTaxonType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Children:
        taxon: List[ChildTaxonType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Synonym:
        """
        :ivar type: The name type.
        :ivar name: The name.
        """
        type: Optional[SynonymType] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class Taxon(TaxonType):
    class Meta:
        name = "taxon"


@dataclass
class TaxonSet:
    class Meta:
        name = "taxonSet"

    taxon: List[TaxonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
