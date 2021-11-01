from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from graflipy.ega.schema_1_5_0.sra_common import IdentifierType


class ChecklistTypeChecklistType(Enum):
    SAMPLE = "Sample"


class FieldGroupRestrictionType(Enum):
    ANY_NUMBER_OR_NONE_OF_THE_FIELDS = "Any number or none of the fields"
    ONE_OF_THE_FIELDS = "One of the fields"
    AT_LEAST_ONE_OF_THE_FIELDS = "At least one of the fields"
    ONE_OR_NONE_OF_THE_FIELDS = "One or none of the fields"


class FieldMandatory(Enum):
    """
    :cvar MANDATORY: Random sequencing of the whole genome.
    :cvar RECOMMENDED: Random sequencing of exonic regions selected from
        the genome.
    :cvar OPTIONAL_VALUE: Random sequencing of whole transcriptome.
    """
    MANDATORY = "mandatory"
    RECOMMENDED = "recommended"
    OPTIONAL_VALUE = "optional"


class FieldMultiplicity(Enum):
    SINGLE = "single"
    MULTIPLE = "multiple"


class TaxonFieldRestrictionType(Enum):
    PERMITTED_TAXA = "Permitted taxa"
    NOT_PERMITTED_TAXA = "Not permitted taxa"


@dataclass
class ChecklistType:
    """
    :ivar identifiers:
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
    :ivar checklist_type:
    """
    identifiers: Optional[IdentifierType] = field(
        default=None,
        metadata={
            "name": "IDENTIFIERS",
            "type": "Element",
            "namespace": "",
        }
    )
    descriptor: Optional["ChecklistType.Descriptor"] = field(
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
    checklist_type: Optional[ChecklistTypeChecklistType] = field(
        default=None,
        metadata={
            "name": "checklistType",
            "type": "Attribute",
        }
    )

    @dataclass
    class Descriptor:
        """
        :ivar label: A unique immutable label for the checklist used for
            referencing purposes.
        :ivar name: The name of the checklist used for display purposes.
        :ivar description: The description of the checklist used for
            display purposes.
        :ivar authority: The checklist authority.
        :ivar field_group: Checklist field group.
        :ivar condition: Field condition.
        """
        label: Optional[str] = field(
            default=None,
            metadata={
                "name": "LABEL",
                "type": "Element",
                "namespace": "",
                "required": True,
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
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "DESCRIPTION",
                "type": "Element",
                "namespace": "",
            }
        )
        authority: Optional[str] = field(
            default=None,
            metadata={
                "name": "AUTHORITY",
                "type": "Element",
                "namespace": "",
            }
        )
        field_group: List["ChecklistType.Descriptor.FieldGroup"] = field(
            default_factory=list,
            metadata={
                "name": "FIELD_GROUP",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        condition: List["ChecklistType.Descriptor.Condition"] = field(
            default_factory=list,
            metadata={
                "name": "CONDITION",
                "type": "Element",
                "namespace": "",
            }
        )

        @dataclass
        class FieldGroup:
            """
            :ivar name: The name of the checklist group for display
                purposes.
            :ivar description: The description of the field group for
                display purposes.
            :ivar field_value: A checklist field.
            :ivar restriction_type:
            """
            name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NAME",
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
            field_value: List["ChecklistType.Descriptor.FieldGroup.FieldType"] = field(
                default_factory=list,
                metadata={
                    "name": "FIELD",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                }
            )
            restriction_type: Optional[FieldGroupRestrictionType] = field(
                default=None,
                metadata={
                    "name": "restrictionType",
                    "type": "Attribute",
                }
            )

            @dataclass
            class FieldType:
                """
                :ivar label: A unique immutable label for the field for
                    referencing purposes.
                :ivar synonym: Synonym that will be converted to LABEL.
                :ivar name: The name of the field for display purposes.
                :ivar description: The description of the field for
                    display purposes.
                :ivar units: The allowed units.
                :ivar field_type: The field type.
                :ivar mandatory: Defines if the attribute is mandatory,
                    recommended or optional.
                :ivar multiplicity: The attribute can appear more than
                    once if the multiplicity value is set to multiple
                    and at most once if the value is set to single. By
                    default an attribute can occur no more than once.
                """
                label: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "LABEL",
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )
                synonym: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "SYNONYM",
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
                description: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "DESCRIPTION",
                        "type": "Element",
                        "namespace": "",
                    }
                )
                units: Optional["ChecklistType.Descriptor.FieldGroup.FieldType.Units"] = field(
                    default=None,
                    metadata={
                        "name": "UNITS",
                        "type": "Element",
                        "namespace": "",
                    }
                )
                field_type: Optional["ChecklistType.Descriptor.FieldGroup.FieldType.FieldType"] = field(
                    default=None,
                    metadata={
                        "name": "FIELD_TYPE",
                        "type": "Element",
                        "namespace": "",
                    }
                )
                mandatory: Optional[FieldMandatory] = field(
                    default=None,
                    metadata={
                        "name": "MANDATORY",
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )
                multiplicity: Optional[FieldMultiplicity] = field(
                    default=None,
                    metadata={
                        "name": "MULTIPLICITY",
                        "type": "Element",
                        "namespace": "",
                        "required": True,
                    }
                )

                @dataclass
                class Units:
                    unit: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "UNIT",
                            "type": "Element",
                            "namespace": "",
                            "min_occurs": 1,
                        }
                    )

                @dataclass
                class FieldType:
                    """
                    :ivar text_field: A single-line text field.
                    :ivar text_area_field: A multi-line text field.
                    :ivar text_choice_field: A single-line text field
                        controlled by a list of text values.
                    :ivar date_field: A date field.
                    :ivar taxon_field: A taxon field.
                    :ivar ontology_field: An ontology field.
                    """
                    text_field: Optional["ChecklistType.Descriptor.FieldGroup.FieldType.FieldType.TextField"] = field(
                        default=None,
                        metadata={
                            "name": "TEXT_FIELD",
                            "type": "Element",
                            "namespace": "",
                        }
                    )
                    text_area_field: Optional["ChecklistType.Descriptor.FieldGroup.FieldType.FieldType.TextAreaField"] = field(
                        default=None,
                        metadata={
                            "name": "TEXT_AREA_FIELD",
                            "type": "Element",
                            "namespace": "",
                        }
                    )
                    text_choice_field: Optional["ChecklistType.Descriptor.FieldGroup.FieldType.FieldType.TextChoiceField"] = field(
                        default=None,
                        metadata={
                            "name": "TEXT_CHOICE_FIELD",
                            "type": "Element",
                            "namespace": "",
                        }
                    )
                    date_field: Optional[object] = field(
                        default=None,
                        metadata={
                            "name": "DATE_FIELD",
                            "type": "Element",
                            "namespace": "",
                        }
                    )
                    taxon_field: Optional["ChecklistType.Descriptor.FieldGroup.FieldType.FieldType.TaxonField"] = field(
                        default=None,
                        metadata={
                            "name": "TAXON_FIELD",
                            "type": "Element",
                            "namespace": "",
                        }
                    )
                    ontology_field: Optional["ChecklistType.Descriptor.FieldGroup.FieldType.FieldType.OntologyField"] = field(
                        default=None,
                        metadata={
                            "name": "ONTOLOGY_FIELD",
                            "type": "Element",
                            "namespace": "",
                        }
                    )

                    @dataclass
                    class TextField:
                        """
                        :ivar min_length: Minimum string length.
                        :ivar max_length: Maximum string length.
                        :ivar regex_value: The regular expression.
                        """
                        min_length: Optional[int] = field(
                            default=None,
                            metadata={
                                "name": "MIN_LENGTH",
                                "type": "Element",
                                "namespace": "",
                            }
                        )
                        max_length: Optional[int] = field(
                            default=None,
                            metadata={
                                "name": "MAX_LENGTH",
                                "type": "Element",
                                "namespace": "",
                            }
                        )
                        regex_value: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "REGEX_VALUE",
                                "type": "Element",
                                "namespace": "",
                            }
                        )

                    @dataclass
                    class TextAreaField:
                        """
                        :ivar min_length: Minimum string length.
                        :ivar max_length: Maximum string length.
                        """
                        min_length: Optional[int] = field(
                            default=None,
                            metadata={
                                "name": "MIN_LENGTH",
                                "type": "Element",
                                "namespace": "",
                            }
                        )
                        max_length: Optional[int] = field(
                            default=None,
                            metadata={
                                "name": "MAX_LENGTH",
                                "type": "Element",
                                "namespace": "",
                            }
                        )

                    @dataclass
                    class TextChoiceField:
                        text_value: List["ChecklistType.Descriptor.FieldGroup.FieldType.FieldType.TextChoiceField.TextValue"] = field(
                            default_factory=list,
                            metadata={
                                "name": "TEXT_VALUE",
                                "type": "Element",
                                "namespace": "",
                                "min_occurs": 1,
                            }
                        )

                        @dataclass
                        class TextValue:
                            """
                            :ivar value: Allowed text value.
                            :ivar synonym: Synonym that will be
                                converted to VALUE.
                            """
                            value: Optional[str] = field(
                                default=None,
                                metadata={
                                    "name": "VALUE",
                                    "type": "Element",
                                    "namespace": "",
                                    "required": True,
                                }
                            )
                            synonym: List[str] = field(
                                default_factory=list,
                                metadata={
                                    "name": "SYNONYM",
                                    "type": "Element",
                                    "namespace": "",
                                }
                            )

                    @dataclass
                    class TaxonField:
                        """
                        :ivar taxon: Taxid.
                        :ivar restriction_type: Taxon restriction type.
                        """
                        taxon: List[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "TAXON",
                                "type": "Element",
                                "namespace": "",
                            }
                        )
                        restriction_type: Optional[TaxonFieldRestrictionType] = field(
                            default=None,
                            metadata={
                                "name": "restrictionType",
                                "type": "Attribute",
                            }
                        )

                    @dataclass
                    class OntologyField:
                        """
                        :ivar label: A unique immutable label for the
                            ontology for referencing purposes.
                        :ivar name: The name of the ontology for display
                            purposes.
                        :ivar description: The description of the
                            ontology for display purposes.
                        """
                        label: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "LABEL",
                                "type": "Element",
                                "namespace": "",
                                "required": True,
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
                        description: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "DESCRIPTION",
                                "type": "Element",
                                "namespace": "",
                            }
                        )

        @dataclass
        class Condition:
            """
            :ivar label: A unique immutable label for referencing
                purposes.
            :ivar name: The name of the condition for display purposes.
            :ivar description: The description of the condition for
                display purposes.
            :ivar expression: The condition expression.
            :ivar error: The condition error.
            """
            label: Optional[str] = field(
                default=None,
                metadata={
                    "name": "LABEL",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
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
            description: Optional[str] = field(
                default=None,
                metadata={
                    "name": "DESCRIPTION",
                    "type": "Element",
                    "namespace": "",
                }
            )
            expression: Optional[str] = field(
                default=None,
                metadata={
                    "name": "EXPRESSION",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )
            error: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ERROR",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                }
            )


@dataclass
class Checklist(ChecklistType):
    class Meta:
        name = "CHECKLIST"


@dataclass
class ChecklistSetType:
    checklist: List[ChecklistType] = field(
        default_factory=list,
        metadata={
            "name": "CHECKLIST",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ChecklistSet(ChecklistSetType):
    class Meta:
        name = "CHECKLIST_SET"
