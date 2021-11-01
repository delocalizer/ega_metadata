"""
Schema packages below here are generated with xsdata.
e.g.
    # cd [PACKAGEROOT] # i.e. src/
    workdir=/tmp
    wget -P $workdir \
        https://github.com/enasequence/schema/archive/refs/tags/1.5.0.tar.gz
    tar -xzvf $workdir/1.5.0.tar.gz --directory $workdir
    xsdata generate -p graflipy.ega.schema_1_5_0 \
        $workdir/schema-1.5.0/src/main/resources/uk/ac/ebi/ena/sra/schema

`*XSD` locations are added manually to `schema_x_y_z/__init__.py`
"""
import logging
import re

from argparse import ArgumentTypeError
from pathlib import Path
from lxml import etree
from xsdata.formats.converter import Converter, converter

from graflipy import (ALIGNEDREADGROUPSET,
                      COLLECTEDSAMPLE,
                      AlignedReadGroupSet,
                      CollectedSample)
from graflipy.exceptions import NotifiableError
from graflipy.orm.persistence import bulk_merge


ERR_ACCESSION_CONFLICT = '%s existing accession %s conflicts with new value %s'
ERR_NOT_FOUND = '%s: %s implied %s not found in db'
ERR_NO_MATCH = '%s does not match %s'
LOGGER = logging.getLogger(__name__)
MSG_ACCESSION_UPDATE = '%s egaAccession marked for update: %s'
MSG_ACCESSION_NOT_FOUND = 'no accessions found in input'
MSG_UPDATE_NOT_REQUIRED = 'update not required, %s already has accession %s'
RE_EGAANALYSIS = re.compile(r'EGAZ\d{11}')
RE_EGAPOLICY = re.compile(r'EGAP\d{11}')
RE_EGASTUDY = re.compile(r'EGAS\d{11}')


class AccessionUpdateError(NotifiableError):
    """
    Raise for problem adding accession to the database, e.g. entity not found
    or conflicting existing accession
    """


class MetadataConstructionError(NotifiableError):
    """
    Raise when insufficient metadata can be found for an object
    """


class PathConverter(Converter):
    """
    Convert pathlib.Path
    """
    def deserialize(self, value: str, **kwargs):
        return Path(value)

    def serialize(self, value: Path, **kwargs):
        return str(value)


converter.register_converter(Path, PathConverter())


def analysis_accession(value):
    """
    Validate EGA analysis accession as argparse argument
    """
    if not RE_EGAANALYSIS.match(value):
        raise ArgumentTypeError(ERR_NO_MATCH % (value, RE_EGAANALYSIS.pattern))
    return value


def policy_accession(value):
    """
    Validate EGA policy accession as argparse argument
    """
    if not RE_EGAPOLICY.match(value):
        raise ArgumentTypeError(ERR_NO_MATCH % (value, RE_EGAPOLICY.pattern))
    return value


def study_accession(value):
    """
    Validate EGA study accession as argparse argument
    """
    if not RE_EGASTUDY.match(value):
        raise ArgumentTypeError(ERR_NO_MATCH % (value, RE_EGASTUDY.pattern))
    return value


def update_accessions(receiptxml):
    """
    Update the database with accessions from the EGA receipt.

    Args:
        receiptxml: file-like binary stream with receipt XML from a submission
            containing ANALYSIS and/or SAMPLE elements with "alias" and
            "accession" attributes. The "alias" attribute value is assumed
            to be the uuid of an entity in the database.
    Raises:
        `AccessionUpdateError` if any of the implied entities were not found
            in the db, or an element `accession` attribute conflicts with an
            existing entity `:egaAccession` property value
    """
    tree = etree.parse(receiptxml)
    tag_class_prefix = (
        ('SAMPLE', CollectedSample, COLLECTEDSAMPLE),
        ('ANALYSIS', AlignedReadGroupSet, ALIGNEDREADGROUPSET)
    )
    errors, updates, found = [], [], False
    for tag, cls, prefix in tag_class_prefix:
        for elem in (tree.findall(f'//{tag}') or []):
            found = True
            alias = elem.attrib['alias']
            accessionupdate = elem.attrib['accession']
            iri = prefix[alias]
            obj = cls.find(iri)
            accessionexists = obj and obj.egaAccession
            if not obj:
                errors.append(ERR_NOT_FOUND % (tag, alias, iri))
            elif accessionexists and accessionupdate != accessionexists:
                errors.append(ERR_ACCESSION_CONFLICT %
                              (obj, accessionexists, accessionupdate))
            elif not accessionexists:
                LOGGER.info(MSG_ACCESSION_UPDATE, iri, accessionupdate)
                obj.egaAccession = accessionupdate
                updates.append(obj)
            else:
                LOGGER.info(MSG_UPDATE_NOT_REQUIRED, iri, accessionexists)
    if errors:
        raise AccessionUpdateError('\n'.join(errors))
    if updates:
        bulk_merge(updates)
    elif not found:
        LOGGER.warning(MSG_ACCESSION_NOT_FOUND)
