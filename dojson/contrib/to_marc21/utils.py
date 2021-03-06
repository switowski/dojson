# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Utilities for converting to MARC21."""

import pkg_resources
from lxml import etree
from lxml.builder import E
from six import iteritems, string_types

from dojson.utils import GroupableOrderedDict

MARC21_DTD = pkg_resources.resource_filename(
    'dojson.contrib.marc21', 'MARC21slim.dtd')
"""Location of the MARC21 DTD file"""

MARC21_NS = "http://www.loc.gov/MARC21/slim"
"""MARCXML XML Schema"""


def dumps_etree(records, xslt_filename=None):
    """Dump records into a etree."""
    root = etree.Element('collection', nsmap={None: MARC21_NS})

    records = [records] if isinstance(records, dict) else records

    for record in records:
        rec = E.record()

        if isinstance(record, GroupableOrderedDict):
            items = record.iteritems(with_order=False, repeated=True)
        else:
            items = iteritems(record)

        for df, subfields in items:
            # Control fields
            if len(df) == 3:
                if isinstance(subfields, string_types):
                    controlfield = E.controlfield(subfields)
                    controlfield.attrib['tag'] = df[0:3]
                    rec.append(controlfield)
                elif isinstance(subfields, (list, tuple, set)):
                    for subfield in subfields:
                        controlfield = E.controlfield(subfield)
                        controlfield.attrib['tag'] = df[0:3]
                        rec.append(controlfield)
            else:
                if not isinstance(subfields, (list, tuple, set)):
                    subfields = (subfields,)

                df = df.replace('_', ' ')
                for subfield in subfields:
                    if not isinstance(subfield, (list, tuple, set)):
                        subfield = [subfield]

                    for s in subfield:
                        datafield = E.datafield()
                        datafield.attrib['tag'] = df[0:3]
                        datafield.attrib['ind1'] = df[3]
                        datafield.attrib['ind2'] = df[4]

                        if isinstance(s, GroupableOrderedDict):
                            items = s.iteritems(with_order=False, repeated=True)
                        elif isinstance(s, dict):
                            items = iteritems(s)
                        else:
                            datafield.append(E.subfield(s))

                            items = tuple()

                        for code, value in items:
                            if not isinstance(value, string_types):
                                for v in value:
                                    datafield.append(E.subfield(v, code=code))
                            else:
                                datafield.append(E.subfield(value, code=code))

                        rec.append(datafield)
        root.append(rec)

    if xslt_filename is not None:
        xslt_root = etree.parse(open(xslt_filename))
        transform = etree.XSLT(xslt_root)
        root = transform(root).getroot()

    return root


def dumps(records, xslt_filename=None, **kwargs):
    """Dump records into a MarcXML file."""
    root = dumps_etree(records=records, xslt_filename=xslt_filename)
    return etree.tostring(root, **kwargs)
