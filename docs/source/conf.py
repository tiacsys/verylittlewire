# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))


# -- Project information -----------------------------------------------------

project = "Little Wire Python library"
copyright = "2022 TiaC Systems members and individual contributors"
author = "TiaC Systems"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.spelling",
    "linuxdoc.rstFlatTable",
    "myst_parser",
]

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [""]

# Enable TO-DO items and list them with a link to the original entry.
todo_include_todos = True
todo_link_only = True

# Prefix each (auto) section label with the name of the document it is in.
autosectionlabel_prefix_document = True

# Suppress arbitrary warning messages.
suppress_warnings = [
    # autogenerated changelog comes with multiple equal head lines, eg. Fixes
    "autosectionlabel.changelog",
]

# Let the spell checker show its suggestions for misspelled words, emitt all
# findings as Sphinx warning and use an additional (project) word list.
spelling_word_list_filename = [os.path.abspath("../spelling_wordlist.txt")]
spelling_show_suggestions = True
spelling_warning = True

# Setup shorten external links and emits a warning if not used.
extlinks_detect_hardcoded_links = True
extlinks = {
    "lwfw11": (
        "https://github.com/littlewire/Little-Wire/blob"
        + "/v1.1/firmware/source/main.c#L%s",
        "main.c:%s",
    ),
    "lwfw12": (
        "https://github.com/littlewire/Little-Wire/blob/v1.2/firmware/main.c#L%s",
        "main.c:%s",
    ),
    "lwcapi": (
        "https://littlewire.github.io/documentation/%s",
        "Little Wire API Reference (%s)",
    ),
    "avrdude70": (
        "https://github.com/avrdudes/avrdude/blob/v7.0/src/usbtiny.c#L%s",
        "usbtiny.c:%s",
    ),
}

# Fine tuning for Sphinx link checker.
linkcheck_ignore = [r"http://localhost:\d+/"]
linkcheck_allowed_redirects = {
    # All HTTP redirections from the source URI to the canonical URI
    # will be treated as "working".
    r"https://sphinx-doc\.org/.*": r"https://sphinx-doc\.org/en/master/.*",
    r"https://github\.com/audreyr/.*": r"https://github\.com/cookiecutter/.*",
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# vim: tw=80 ts=4 sw=4 sts=4 sta et ai nu
