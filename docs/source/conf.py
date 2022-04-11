# pylint: skip-file
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

sys.path.insert(0, os.path.abspath("./../../python-template-repo"))

# IF you have a specific tree structured, you might need to add your
# module's path manually if sphinx does'nt find them
# module_paths = ["../../python-template-repo"]
# exclude_modules = ["app_example", "other_module"]
# for module_path in module_paths:
#     for dir in os.listdir(module_path):
#         if dir not in exclude_modules:
#             sys.path.insert(
#                 0, os.path.abspath(os.path.join(os.path.join(module_path, dir), dir))
#             )

# -- Project information -----------------------------------------------------

project = "python_template_repo"
copyright = "2022, Etienne de Montalivet"
author = "Etienne de Montalivet"

# The full version, including alpha/beta/rc tags
release = "0.1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "numpydoc",
    "sphinx.ext.autosectionlabel",
]

# copy code button settings: this won't be copied
copybutton_prompt_text = ">>> "

# numpydoc_class_members_toctree = True
# numpydoc_show_class_members = True
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 10

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autosummary_imported_members = False
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
exclude_patterns = ["_build", "_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
source_suffix = [".rst", ".md"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
