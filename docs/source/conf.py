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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = '20m Docs'
copyright = '2024, Green Bank Observatory, A. Schmiedeke'
author = 'Green Bank Observatory'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 
              'sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.napoleon',
              'sphinx.ext.autosummary',
              'sphinx.ext.mathjax',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel',
              'sphinx_design',
              'sphinx_copybutton',
              'sphinx_inline_tabs'
]


autosummary_generate = False
add_module_names = False
toc_object_entries_show_parents = 'hide'

todo_include_todos = True

intersphinx_mapping = {
        'dysh': ("https://dysh.readthedocs.io/en/latest", None)
}

intersphinx_disabled_reftypes = ["*"]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['css/custom.css']

html_logo = '_static/GBO-vertical-PGGradient.svg'

#html_theme_options = {
#    "logo": {
#        "image_light": "", 
#        "image_dark": "", 
#    }
#}


# -- Options for latexpdf output ---------------------------------------------

latex_use_parts=True
