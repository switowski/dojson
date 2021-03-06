Changes
=======

Version 1.0.1 (released 2016-01-19):
------------------------------------

Bug fixes
~~~~~~~~~

- Fixes support for Python 3.5.1.

Version 1.0.0 (released 2016-01-14):
------------------------------------

Incompatible changes
~~~~~~~~~~~~~~~~~~~~

- Removes support for single key matching multiple rules. Please make
  your rules mutually exclusive!
- controlfields 00x are expected to be the element or a list of
  multiple elements.

New features
~~~~~~~~~~~~

- Adds new keyword argument `ignore_missing` to `Overdo.do` method to
  specify if method should raise `MissingRule` exception when there is
  no matching rule for a key.
- Adds new CLI option `--strict` to the `do` command that sets the
  `ignore_missing` argument to `False`.  (#51)
- MARC XML serialization from to_marc21.

Improved features
~~~~~~~~~~~~~~~~~

- Adds support for Python 3+.
- Uses an OrderedDict to let the external tools working on `dict`
  (like json) behave correctly.
- All results from rules using `for_each_value` decorator are being
  automatically extended. This is useful for repeatable MARC21 fields
  with different indicators.  (#53)
- Record are stored in an immutable sorted structure which enables to
  keep the intended order while offering easy ways to access, index
  and manipulate.
- Adds two records to be tested.
- Reorders some of the assertion: `expected == actual`.

Version 0.4.0 (released 2015-11-18):
------------------------------------

New features
~~~~~~~~~~~~

- Improves dojson.contrib.marc2.utils.load() to read the input by
  iterating of the open stream, rather than loading it all in memory
  in one go.  (#45) (#46)
- Renames OverUndo to Underdo following same name convention as for
  Overdo.

Bug fixes
~~~~~~~~~

- Fixes indicator extraction from value in `Underdo` model.

Version 0.3.0 (released 2015-11-09):
------------------------------------

New features
~~~~~~~~~~~~

- Adds **experimental** rules for converting human readable JSON into
  a JSON representation of the MARC21 Format.
- Adds `do` and `missing` commands for `dojson` command line interface
  (see `dojson --help` for more information).

Improved features
~~~~~~~~~~~~~~~~~

- Adds missing mapping for the first indicator of field 856.

Version 0.2.0 (released 2015-10-07):
------------------------------------

New features
~~~~~~~~~~~~

- Adds the posibility to use base DoJSON model so the rules are
  "inherited" from them.
- Adds new decorator `ignore_value` that remove the key in the
  resulting json for None value.

Improved features
~~~~~~~~~~~~~~~~~

- Uses entry points instead of plain imports to load the creator
  rules.

Bug fixes
~~~~~~~~~

- Removes calls to PluginManager consider_setuptools_entrypoints()
  removed in PyTest 2.8.0.

Version 0.1.1 (released 2015-07-27):
------------------------------------

- Sorts and removes duplicated enum values.
- Swaps wrongly defined repeatable and non-repeatable subfields. (#23)
- Addresses issue when allowed indicators where defined as a range.
  (#22)

Version 0.1.0 (released 2015-07-03):
------------------------------------

- Initial public release.
