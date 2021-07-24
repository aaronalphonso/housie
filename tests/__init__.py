"""
Before running tests, we need to install our housie package locally. This is so that all the imports in our tests, pick
up the modules from the actual installed copy.

You can do this with either of the following commands:
* `pip install .` - Your tests run against an installed version
* `pip install --editable .` - Your tests run against the local copy with an editable install

The --editable option links the installed version with the local copy of code, so any changes you make to the code are
directly reflected in the installed version. Always use this option when doing development, as you can rapidly make
changes to code and retest without having to uninstall and reinstall the local housie package.
"""
