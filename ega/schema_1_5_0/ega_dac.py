from dataclasses import dataclass, field
from typing import List, Optional
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    IdentifierType,
    LinkType,
)


@dataclass
class DacType:
    """
    Describes an object that contains data access comittee  information
    including contacts.

    :ivar identifiers:
    :ivar title: Short text that can be used to call out DAC records in
        searches or in displays.
    :ivar contacts:
    :ivar dac_links: Links to related resources.
    :ivar dac_attributes: Properties and attributes of the DAC. These
        can be entered as free-form tag-value pairs. Submitters may be
        asked to follow a community established ontology when describing
        the work.
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
    contacts: Optional["DacType.Contacts"] = field(
        default=None,
        metadata={
            "name": "CONTACTS",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dac_links: Optional["DacType.DacLinks"] = field(
        default=None,
        metadata={
            "name": "DAC_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )
    dac_attributes: Optional["DacType.DacAttributes"] = field(
        default=None,
        metadata={
            "name": "DAC_ATTRIBUTES",
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
    class Contacts:
        contact: List["DacType.Contacts.Contact"] = field(
            default_factory=list,
            metadata={
                "name": "CONTACT",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Contact:
            """
            :ivar name: Name of contact person for this DAC.
            :ivar email: email of the person to contact.
            :ivar telephone_number: telephone_number of the person to
                contact.
            :ivar organisation: Center or institution name .
            :ivar main_contact: If true then this is the main contact.
            """
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            telephone_number: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                }
            )
            organisation: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            main_contact: Optional[bool] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                }
            )

    @dataclass
    class DacLinks:
        dac_link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "name": "DAC_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class DacAttributes:
        dac_attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "name": "DAC_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class Dac(DacType):
    class Meta:
        name = "DAC"


@dataclass
class DacSetType:
    dac: List[Dac] = field(
        default_factory=list,
        metadata={
            "name": "DAC",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class DacSet(DacSetType):
    """
    Container for a set of data access policies.
    """
    class Meta:
        name = "DAC_SET"
