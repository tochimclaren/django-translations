# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import json
import datetime

# `Django setup` below, will add the path to `translations` module
# automatically because it's been included in `project.settings`, so no need
# to import it here

# -- Django setup ------------------------------------------------------------

# generated project settings
import django

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath('.')), 'project')
)
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
django.setup()

# -- Project information -----------------------------------------------------

with open(
        os.path.join(
            os.path.dirname(os.path.abspath('.')),
            'config.json'
        ), 'r') as fh:
    info = json.load(fh)


# project
project = info['project']['name']

# description
description = info['project']['desc']

# author
author = info['author']['name']

# The short X.Y version
version = info['release']['version']

# The full version, including alpha/beta/rc tags
release = info['release']['name']

# github
github_user = info['github']['user']
github_repo = info['github']['repo']

# donation
donate_url = info['urls']['funding']

# logo
logo = info['project']['logo']

# documentation
documentation = '{} {}'.format(project, 'Documentation')

# year
year = datetime.datetime.now().year

# copyright
copyright = '{year}, {author}'.format(year=year, author=author)

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'note_bg': '#fec',
    'note_border': '#ffe2a8',
    'pre_bg': '#f7f7f7',
    'show_relbars': True,
    'fixed_sidebar': True,
    'logo': logo,
    'touch_icon': logo,
    'logo_name': True,
    'description': description,
    'github_user': github_user,
    'github_repo': github_repo,
    'github_banner': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DjangoTranslationsdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'DjangoTranslations.tex', documentation,
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'djangotranslations', documentation,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'DjangoTranslations', documentation,
     author, 'DjangoTranslations', description,
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'django': ('http://django.readthedocs.org/en/latest/', None),
}

# -- Options for doctest extension -------------------------------------------

doctest_global_setup = """
from django.db import connection
from django.test import TestCase
from django.db.models.query import QuerySet
from pprint import pprint
import builtins

# Turn on the test database for the doctests
connection.creation.create_test_db(verbosity=0)
TestCase.setUpClass()

# Beautify `testoutput`
def print(obj=''):
    if type(obj) == dict:
        pprint(obj, width=72)
    elif type(obj) == QuerySet:
        obj = obj.order_by('id')
        representation = repr(obj)
        start_index = representation.find('[')
        end_index = representation.rfind(']')
        start = representation[:(start_index + 1)]
        center = representation[(start_index + 1): end_index]
        end = representation[end_index:]
        items = map(lambda x: (' ' * 4) + x, center.split(', '))
        print(start)
        print(',\\n'.join(items))
        print(end)
    else:
        builtins.print(obj)

"""

doctest_global_cleanup = """
from django.db import connection
from django.test import TestCase

# Turn off the test database for the doctests
TestCase.tearDownClass()
connection.creation.destroy_test_db(verbosity=0)
"""
