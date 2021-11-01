from dataclasses import dataclass, field
from typing import List, Optional
from graflipy.ega.schema_1_5_0.sra_common import IdentifierType


@dataclass
class SampleGroupType:
    """
    :ivar identifiers:
    :ivar title: Title of the sample group which will be displayed in
        database search results.
    :ivar description: Describes the sample group in detail.
    :ivar descriptor:
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
    descriptor: Optional["SampleGroupType.Descriptor"] = field(
        default=None,
        metadata={
            "name": "DESCRIPTOR",
            "type": "Element",
            "namespace": "",
            "required": True,
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
    class Descriptor:
        """
        :ivar checklist_ref: The checklist.
        :ivar checklist_attribute:
        :ivar study_ref:
        :ivar sample_ref: One of more samples associated with the sample
            group.
        """
        checklist_ref: Optional["SampleGroupType.Descriptor.ChecklistRef"] = field(
            default=None,
            metadata={
                "name": "CHECKLIST_REF",
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )
        checklist_attribute: List["SampleGroupType.Descriptor.ChecklistAttribute"] = field(
            default_factory=list,
            metadata={
                "name": "CHECKLIST_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
            }
        )
        study_ref: Optional["SampleGroupType.Descriptor.StudyRef"] = field(
            default=None,
            metadata={
                "name": "STUDY_REF",
                "type": "Element",
                "namespace": "",
            }
        )
        sample_ref: List["SampleGroupType.Descriptor.SampleRef"] = field(
            default_factory=list,
            metadata={
                "name": "SAMPLE_REF",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

        @dataclass
        class ChecklistRef:
            """
            :ivar identifiers:
            :ivar alias: Submitter designated name of the SRA document
                of this type.  At minimum alias should be unique
                throughout the submission of this document type.  If
                center_name is specified, the name should be unique in
                all submissions from that center of this document type.
            :ivar center_name: Owner authority of this document and
                namespace for submitter's name of this document.  If not
                provided, then the submitter is regarded as "Individual"
                and document resolution can only happen within the
                submission.
            :ivar broker_name: Broker authority of this document.  If
                not provided, then the broker is considered "direct".
            :ivar accession: The document's accession as assigned by the
                Home Archive.
            """
            identifiers: Optional[IdentifierType] = field(
                default=None,
                metadata={
                    "name": "IDENTIFIERS",
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
        class ChecklistAttribute:
            """
            :ivar tag: Name of the attribute.
            :ivar unit: Selected unit.
            """
            tag: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TAG",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            unit: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UNIT",
                    "type": "Element",
                    "namespace": "",
                }
            )

        @dataclass
        class StudyRef:
            """
            :ivar identifiers:
            :ivar refname: Identifies a record by name that is known
                within the namespace defined by attribute "refcenter"
                Use this field when referencing an object for which an
                accession has not yet been issued.
            :ivar refcenter: The center namespace of the attribute
                "refname". When absent, the namespace is assumed to be
                the current submission.
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
            :ivar refname: Identifies a record by name that is known
                within the namespace defined by attribute "refcenter"
                Use this field when referencing an object for which an
                accession has not yet been issued.
            :ivar refcenter: The center namespace of the attribute
                "refname". When absent, the namespace is assumed to be
                the current submission.
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
class SampleGroup(SampleGroupType):
    class Meta:
        name = "SAMPLE_GROUP"


@dataclass
class SampleGroupSetType:
    sample_group: List[SampleGroupType] = field(
        default_factory=list,
        metadata={
            "name": "SAMPLE_GROUP",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class SampleGroupSet(SampleGroupSetType):
    class Meta:
        name = "SAMPLE_GROUP_SET"
