from dataclasses import dataclass, field
from typing import List, Optional
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    IdentifierType,
    LinkType,
)


@dataclass
class PolicyType:
    """
    Describes an object that contains data access policy information.

    :ivar identifiers:
    :ivar title: Short text that can be used to call out data access
        policies in searches or in displays.
    :ivar dac_ref: The DAC_REF identifies the data access committee to
        which this policy pertains.
    :ivar policy_text: Text containing the policy.
    :ivar policy_file: File containing the policy text.
    :ivar policy_links: Links to related resources.
    :ivar policy_attributes: Properties and attributes of the policy.
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
    dac_ref: Optional["PolicyType.DacRef"] = field(
        default=None,
        metadata={
            "name": "DAC_REF",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    policy_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "POLICY_TEXT",
            "type": "Element",
            "namespace": "",
        }
    )
    policy_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "POLICY_FILE",
            "type": "Element",
            "namespace": "",
        }
    )
    policy_links: Optional["PolicyType.PolicyLinks"] = field(
        default=None,
        metadata={
            "name": "POLICY_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )
    policy_attributes: Optional["PolicyType.PolicyAttributes"] = field(
        default=None,
        metadata={
            "name": "POLICY_ATTRIBUTES",
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
    class DacRef:
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
    class PolicyLinks:
        policy_link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "name": "POLICY_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class PolicyAttributes:
        policy_attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "name": "POLICY_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class Policy(PolicyType):
    """
    Data access policy.
    """
    class Meta:
        name = "POLICY"


@dataclass
class PolicySetType:
    policy: List[Policy] = field(
        default_factory=list,
        metadata={
            "name": "POLICY",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PolicySet(PolicySetType):
    """
    Container for a set of data access policies.
    """
    class Meta:
        name = "POLICY_SET"
