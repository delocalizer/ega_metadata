from dataclasses import dataclass, field
from typing import List, Optional
from graflipy.ega.schema_1_5_0.sra_common import (
    AttributeType,
    IdentifierType,
    LinkType,
)


@dataclass
class SampleType:
    """A Sample defines an isolate of sequenceable material upon which
    sequencing experiments can be based.

    The Sample object may be a surrogate for taxonomy accession or an
    anonymized individual identifier.  Or, it may fully specify
    provenance and isolation method of the starting material.

    :ivar identifiers:
    :ivar title: Short text that can be used to call out sample records
        in search results or in displays.
    :ivar sample_name:
    :ivar description: Free-form text describing the sample, its origin,
        and its method of isolation.
    :ivar sample_links: Links to resources related to this sample or
        sample set (publication, datasets, online databases).
    :ivar sample_attributes: Properties and attributes of a sample.
        These can be entered as free-form  tag-value pairs. For certain
        studies, submitters may be asked to follow a community
        established ontology when describing the work.
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
    sample_name: Optional["SampleType.SampleName"] = field(
        default=None,
        metadata={
            "name": "SAMPLE_NAME",
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
    sample_links: Optional["SampleType.SampleLinks"] = field(
        default=None,
        metadata={
            "name": "SAMPLE_LINKS",
            "type": "Element",
            "namespace": "",
        }
    )
    sample_attributes: Optional["SampleType.SampleAttributes"] = field(
        default=None,
        metadata={
            "name": "SAMPLE_ATTRIBUTES",
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
    class SampleName:
        """
        :ivar taxon_id: NCBI Taxonomy Identifier.  This is appropriate
            for individual organisms and some environmental samples.
        :ivar scientific_name: Scientific name of sample that
            distinguishes its taxonomy.  Please use a  name or synonym
            that is tracked in the INSDC Taxonomy database.  Also, this
            field can be used to confirm the TAXON_ID setting.
        :ivar common_name: GenBank common name of the organism.
            Examples: human, mouse.
        :ivar anonymized_name: Anonymous public name of the sample.
            For example, HapMap human isolate NA12878.
        :ivar individual_name: Individual name of the sample.  This
            field can be used to identify the individual identity of a
            sample where appropriate (this is usually NOT appropriate
            for human subjects).  Example: "Glennie" the platypus.
        """
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
        anonymized_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "ANONYMIZED_NAME",
                "type": "Element",
                "namespace": "",
            }
        )
        individual_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "INDIVIDUAL_NAME",
                "type": "Element",
                "namespace": "",
            }
        )

    @dataclass
    class SampleLinks:
        sample_link: List[LinkType] = field(
            default_factory=list,
            metadata={
                "name": "SAMPLE_LINK",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )

    @dataclass
    class SampleAttributes:
        sample_attribute: List[AttributeType] = field(
            default_factory=list,
            metadata={
                "name": "SAMPLE_ATTRIBUTE",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )


@dataclass
class Sample(SampleType):
    class Meta:
        name = "SAMPLE"


@dataclass
class SampleSetType:
    sample: List[SampleType] = field(
        default_factory=list,
        metadata={
            "name": "SAMPLE",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class SampleSet(SampleSetType):
    """
    SAMPLE_SET serves as a container for a set of samples and a name space for
    establishing referential integrity between them.
    """
    class Meta:
        name = "SAMPLE_SET"
