from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    IdentifierType,
    Urltype,
    XrefType,
)


@dataclass
class OrganismType:
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
            "required": True,
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
    breed: Optional[str] = field(
        default=None,
        metadata={
            "name": "BREED",
            "type": "Element",
            "namespace": "",
        }
    )
    cultivar: Optional[str] = field(
        default=None,
        metadata={
            "name": "CULTIVAR",
            "type": "Element",
            "namespace": "",
        }
    )
    isolate: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISOLATE",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PublicationType:
    unstructured_citation: Optional[str] = field(
        default=None,
        metadata={
            "name": "UNSTRUCTURED_CITATION",
            "type": "Element",
            "namespace": "",
        }
    )
    structured_citation: Optional["PublicationType.StructuredCitation"] = field(
        default=None,
        metadata={
            "name": "STRUCTURED_CITATION",
            "type": "Element",
            "namespace": "",
        }
    )
    publication_links: Optional["PublicationType.PublicationLinks"] = field(
        default=None,
        metadata={
            "name": "PUBLICATION_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class StructuredCitation:
        title: Optional[str] = field(
            default=None,
            metadata={
                "name": "TITLE",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        journal: Optional[str] = field(
            default=None,
            metadata={
                "name": "JOURNAL",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        year: Optional[str] = field(
            default=None,
            metadata={
                "name": "YEAR",
                "type": "Element",
                "namespace": "",
            }
        )
        volume: Optional[str] = field(
            default=None,
            metadata={
                "name": "VOLUME",
                "type": "Element",
                "namespace": "",
            }
        )
        issue: Optional[str] = field(
            default=None,
            metadata={
                "name": "ISSUE",
                "type": "Element",
                "namespace": "",
            }
        )
        first_page: Optional[str] = field(
            default=None,
            metadata={
                "name": "FIRST_PAGE",
                "type": "Element",
                "namespace": "",
            }
        )
        last_page: Optional[str] = field(
            default=None,
            metadata={
                "name": "LAST_PAGE",
                "type": "Element",
                "namespace": "",
            }
        )
        authors: Optional["PublicationType.StructuredCitation.Authors"] = field(
            default=None,
            metadata={
                "name": "AUTHORS",
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class Authors:
            author: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "AUTHOR",
                    "type": "Element",
                    "namespace": "",
                }
            )
            consortium: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "CONSORTIUM",
                    "type": "Element",
                    "namespace": "",
                }
            )

    @dataclass
    class PublicationLinks:
        publication_link: List["PublicationType.PublicationLinks.PublicationLink"] = field(
            default_factory=list,
            metadata={
                "name": "PUBLICATION_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

        @dataclass
        class PublicationLink:
            xref_link: Optional[XrefType] = field(
                default=None,
                metadata={
                    "name": "XREF_LINK",
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class ProjectType:
    """
    :ivar identifiers:
    :ivar name: A short name of the project.
    :ivar title: A short descriptive title for the project.
    :ivar description: A long description of the scope of the project.
    :ivar publications:
    :ivar collaborators:
    :ivar submission_project: A project for grouping submitted data
        together.
    :ivar umbrella_project: A project for grouping other projects
        together.
    :ivar related_projects: Other projects related to this project.
    :ivar project_links:
    :ivar project_attributes:
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
    :ivar first_public:
    """
    identifiers: Optional[IdentifierType] = field(
        default=None,
        metadata={
            "name": "IDENTIFIERS",
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
    publications: Optional["ProjectType.Publications"] = field(
        default=None,
        metadata={
            "name": "PUBLICATIONS",
            "type": "Element",
            "namespace": "",
        }
    )
    collaborators: Optional["ProjectType.Collaborators"] = field(
        default=None,
        metadata={
            "name": "COLLABORATORS",
            "type": "Element",
            "namespace": "",
        }
    )
    submission_project: Optional["ProjectType.SubmissionProject"] = field(
        default=None,
        metadata={
            "name": "SUBMISSION_PROJECT",
            "type": "Element",
            "namespace": "",
        }
    )
    umbrella_project: Optional["ProjectType.UmbrellaProject"] = field(
        default=None,
        metadata={
            "name": "UMBRELLA_PROJECT",
            "type": "Element",
            "namespace": "",
        }
    )
    related_projects: Optional["ProjectType.RelatedProjects"] = field(
        default=None,
        metadata={
            "name": "RELATED_PROJECTS",
            "type": "Element",
            "namespace": "",
        }
    )
    project_links: Optional["ProjectType.ProjectLinks"] = field(
        default=None,
        metadata={
            "name": "PROJECT_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )
    project_attributes: Optional["ProjectType.ProjectAttributes"] = field(
        default=None,
        metadata={
            "name": "PROJECT_ATTRIBUTES",
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
    first_public: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Publications:
        publication: List[PublicationType] = field(
            default_factory=list,
            metadata={
                "name": "PUBLICATION",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Collaborators:
        collaborator: List[str] = field(
            default_factory=list,
            metadata={
                "name": "COLLABORATOR",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class RelatedProjects:
        related_project: List["ProjectType.RelatedProjects.RelatedProject"] = field(
            default_factory=list,
            metadata={
                "name": "RELATED_PROJECT",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

        @dataclass
        class RelatedProject:
            parent_project: Optional["ProjectType.RelatedProjects.RelatedProject.ParentProject"] = field(
                default=None,
                metadata={
                    "name": "PARENT_PROJECT",
                    "type": "Element",
                    "namespace": "",
                }
            )
            child_project: Optional["ProjectType.RelatedProjects.RelatedProject.ChildProject"] = field(
                default=None,
                metadata={
                    "name": "CHILD_PROJECT",
                    "type": "Element",
                    "namespace": "",
                }
            )
            peer_project: Optional["ProjectType.RelatedProjects.RelatedProject.PeerProject"] = field(
                default=None,
                metadata={
                    "name": "PEER_PROJECT",
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class ParentProject:
                """
                :ivar accession: Identifies the project using
                    an accession number.
                """
                accession: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class ChildProject:
                """
                :ivar accession: Identifies the project using
                    an accession number.
                """
                accession: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class PeerProject:
                """
                :ivar accession: Identifies the project using
                    an accession number.
                """
                accession: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    }
                )

    @dataclass
    class ProjectLinks:
        project_link: List["ProjectType.ProjectLinks.ProjectLink"] = field(
            default_factory=list,
            metadata={
                "name": "PROJECT_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

        @dataclass
        class ProjectLink:
            xref_link: Optional[XrefType] = field(
                default=None,
                metadata={
                    "name": "XREF_LINK",
                    "type": "Element",
                    "namespace": "",
                }
            )
            url_link: Optional[Urltype] = field(
                default=None,
                metadata={
                    "name": "URL_LINK",
                    "type": "Element",
                    "namespace": "",
                }
            )

    @dataclass
    class ProjectAttributes:
        project_attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "name": "PROJECT_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class SubmissionProject:
        sequencing_project: Optional["ProjectType.SubmissionProject.SequencingProject"] = field(
            default=None,
            metadata={
                "name": "SEQUENCING_PROJECT",
                "type": "Element",
                "namespace": "",
            }
        )
        organism: Optional[OrganismType] = field(
            default=None,
            metadata={
                "name": "ORGANISM",
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class SequencingProject:
            locus_tag_prefix: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "LOCUS_TAG_PREFIX",
                    "type": "Element",
                    "namespace": "",
                }
            )

    @dataclass
    class UmbrellaProject:
        organism: Optional[OrganismType] = field(
            default=None,
            metadata={
                "name": "ORGANISM",
                "type": "Element",
                "namespace": "",
            }
        )


@dataclass
class Project(ProjectType):
    class Meta:
        name = "PROJECT"


@dataclass
class ProjectSetType:
    project: List[ProjectType] = field(
        default_factory=list,
        metadata={
            "name": "PROJECT",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ProjectSet(ProjectSetType):
    class Meta:
        name = "PROJECT_SET"
