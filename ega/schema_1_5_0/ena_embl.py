from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate


class EntryTypeTopology(Enum):
    CIRCULAR = "circular"
    LINEAR = "linear"


@dataclass
class XrefType:
    """
    Database cross-reference.
    """
    db: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    secondary_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "secondaryId",
            "type": "Attribute",
        }
    )


class ReferenceType(Enum):
    SUBMISSION = "submission"
    BOOK = "book"
    ARTICLE = "article"
    PATENT = "patent"
    THESIS = "thesis"
    UNPUBLISHED = "unpublished"


@dataclass
class EntryType:
    """
    :ivar secondary_accession:
    :ivar project_accession:
    :ivar description:
    :ivar comment:
    :ivar keyword:
    :ivar reference: Not supported for EMBL-CDS.
    :ivar xref:
    :ivar feature: Sequence feature.
    :ivar assembly:
    :ivar contig:
    :ivar sequence:
    :ivar accession:
    :ivar version:
    :ivar entry_version: Not supported for EMBL-CDS.
    :ivar data_class:
    :ivar taxonomic_division:
    :ivar molecule_type:
    :ivar sequence_length:
    :ivar topology:
    :ivar first_public: Not supported for EMBL-CDS.
    :ivar first_public_release: Not supported for EMBL-CDS.
    :ivar last_updated: Not supported for EMBL-CDS.
    :ivar last_updated_release: Not supported for EMBL-CDS.
    """
    secondary_accession: List[str] = field(
        default_factory=list,
        metadata={
            "name": "secondaryAccession",
            "type": "Element",
        }
    )
    project_accession: List[str] = field(
        default_factory=list,
        metadata={
            "name": "projectAccession",
            "type": "Element",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reference: List["EntryType.Reference"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    xref: List[XrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    feature: List["EntryType.Feature"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    assembly: Optional["EntryType.Assembly"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contig: Optional["EntryType.Contig"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    accession: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    entry_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "entryVersion",
            "type": "Attribute",
        }
    )
    data_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataClass",
            "type": "Attribute",
            "required": True,
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
    molecule_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "moleculeType",
            "type": "Attribute",
            "required": True,
        }
    )
    sequence_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequenceLength",
            "type": "Attribute",
            "required": True,
        }
    )
    topology: Optional[EntryTypeTopology] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    first_public: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "firstPublic",
            "type": "Attribute",
        }
    )
    first_public_release: Optional[int] = field(
        default=None,
        metadata={
            "name": "firstPublicRelease",
            "type": "Attribute",
        }
    )
    last_updated: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
        }
    )
    last_updated_release: Optional[int] = field(
        default=None,
        metadata={
            "name": "lastUpdatedRelease",
            "type": "Attribute",
        }
    )

    @dataclass
    class Reference:
        """
        :ivar title:
        :ivar author:
        :ivar applicant: Patent applicant.
        :ivar consortium:
        :ivar submission_date: The submission date (used only for
            submission references).
        :ivar journal: The journal name (used only for article
            references).
        :ivar year: The publication year (used only for article
            references).
        :ivar volume: The volume number (used only for article
            references).
        :ivar issue: The issue number (used only for article
            references).
        :ivar first_page: The first page (used only for article
            references).
        :ivar last_page: The last page (used only for article
            references).
        :ivar comment:
        :ivar reference_location:
        :ivar xref:
        :ivar type:
        :ivar number:
        :ivar location:
        """
        title: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        author: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        applicant: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        consortium: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        submission_date: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "submissionDate",
                "type": "Element",
            }
        )
        journal: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        year: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        volume: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        issue: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        first_page: Optional[str] = field(
            default=None,
            metadata={
                "name": "firstPage",
                "type": "Element",
            }
        )
        last_page: Optional[str] = field(
            default=None,
            metadata={
                "name": "lastPage",
                "type": "Element",
            }
        )
        comment: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        reference_location: Optional[str] = field(
            default=None,
            metadata={
                "name": "referenceLocation",
                "type": "Element",
            }
        )
        xref: List[XrefType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        type: Optional[ReferenceType] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        number: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        location: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class Feature:
        """
        :ivar taxon:
        :ivar xref:
        :ivar qualifier: Sequence feature qualifier.
        :ivar name:
        :ivar location:
        """
        taxon: Optional["EntryType.Feature.Taxon"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        xref: List[XrefType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        qualifier: List["EntryType.Feature.Qualifier"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        location: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

        @dataclass
        class Taxon:
            lineage: Optional["EntryType.Feature.Taxon.Lineage"] = field(
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
                }
            )

            @dataclass
            class Lineage:
                taxon: List["EntryType.Feature.Taxon.Lineage.Taxon"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class Taxon:
                    scientific_name: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "scientificName",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

        @dataclass
        class Qualifier:
            value: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
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
    class Assembly:
        range: List["EntryType.Assembly.Range"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Range:
            begin: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            end: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            primary_begin: Optional[int] = field(
                default=None,
                metadata={
                    "name": "primaryBegin",
                    "type": "Attribute",
                }
            )
            primary_end: Optional[int] = field(
                default=None,
                metadata={
                    "name": "primaryEnd",
                    "type": "Attribute",
                }
            )
            accession: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            version: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            complement: bool = field(
                default=False,
                metadata={
                    "type": "Attribute",
                }
            )

    @dataclass
    class Contig:
        range: List["EntryType.Contig.Range"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "sequential": True,
            }
        )
        gap: List["EntryType.Contig.Gap"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "sequential": True,
            }
        )

        @dataclass
        class Range:
            begin: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            end: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            primary_begin: Optional[int] = field(
                default=None,
                metadata={
                    "name": "primaryBegin",
                    "type": "Attribute",
                }
            )
            primary_end: Optional[int] = field(
                default=None,
                metadata={
                    "name": "primaryEnd",
                    "type": "Attribute",
                }
            )
            accession: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            version: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            complement: bool = field(
                default=False,
                metadata={
                    "type": "Attribute",
                }
            )

        @dataclass
        class Gap:
            begin: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            end: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            length: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            unknown_length: bool = field(
                default=False,
                metadata={
                    "name": "unknownLength",
                    "type": "Attribute",
                }
            )


@dataclass
class Entry(EntryType):
    class Meta:
        name = "entry"


@dataclass
class EntrySet:
    class Meta:
        name = "entrySet"

    entry: List[EntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
