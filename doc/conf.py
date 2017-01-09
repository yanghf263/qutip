#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tmp documentation build configuration file, created by
# sphinx-quickstart on Sun Jan  8 21:26:50 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys, os
sys.path.append(os.path.abspath('_sphinxext'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.5'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax',
              'IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive',
              'matplotlib.sphinxext.only_directives',
              'matplotlib.sphinxext.plot_directive',
              'sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.doctest',
              'sphinx.ext.autosummary',
              'numpydoc',
              'sphinx.ext.extlinks',
              'sphinx.ext.viewcode',
              'sphinx.ext.ifconfig',
              'sphinx.ext.napoleon'
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# This is needed for ipython @savefig
# Otherwise it just puts the png in the root dir
savefig_dir = '_images'
ipython_savefig_dir = '_images'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'QuTiP: Quantum Toolbox in Python'
author = 'P.D. Nation, J.R. Johansson, A.J.G. Pitchford, C. Granade, and A.L. Grimsmo'
copyright = u'2011 and later, {}'.format(author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '4.0'
# The full version, including alpha/beta/rc tags.
release = '4.0.2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []
todo_include_todos = True

numpydoc_show_class_members = False
napoleon_numpy_docstring = True
napoleon_use_admonition_for_notes = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
full_logo= True


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
}
# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'QuTiP {} Documentation'.format(version)

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = u'QuTiP'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'figures/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'QuTiPdoc'


# -- Options for LaTeX output ---------------------------------------------

# AJGP 2017-01-8: Switching to manual, ditching the preamble

# latex_header = open('latex_output_files/latex_preamble.tex', 'r+')
# PREAMBLE = latex_header.read();

latex_elements = {
                  'papersize':'a4paper',
                  'pointsize':'10pt',
                  'classoptions': '',
                  'babel': '\\usepackage[english]{babel}',
                  'fncychap' : '',
#                  'preamble': PREAMBLE
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'qutip.tex', project, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'figures/logo.png'

# Suggested during make
latex_keep_old_macro_names=False 

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'qutip', project, [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'qutip', project,
     author, 'QuTiP', 
     'Quantum Toolbox in Python',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

autodoc_member_order = 'alphabetical'

## EXTLINKS CONFIGURATION ######################################################

extlinks = {
    'arxiv': ('http://arxiv.org/abs/%s', 'arXiv:'),
    'doi': ('http://dx.doi.org/%s', 'doi:'),
}

## WORKAROUNDS #################################################################

# To work around ipython/ipython#9339, we register a new "directive" that either
# does exactly what IPythonDirective does, or does syntax highlighting only,
# depending on the hosting OS.

def setup(app):
    import os
    from IPython.sphinxext.ipython_directive import IPythonDirective

    if os.name == "nt":
        from sphinx.directives.code import CodeBlock
        
        class IPythonCodeBlock(CodeBlock):
            required_arguments = 0

            @property
            def arguments(self):
                return ['ipython']
            @arguments.setter
            def arguments(self, newval):
                pass
        app.add_directive('ipython-posix', IPythonCodeBlock)

    else:
        app.add_directive('ipython-posix', IPythonDirective)

# The other workaround we need is that IPython's sphinxext depends on
# pickeshare 0.5 (latest being 0.6), which in turn calls path.path
# instead of path.Path. This results in an entire sea of DeprecationWarnings.
# Since Sphinx overrides warnings filters during the parsing stage, we can't
# disable in a safe or reasonable way; thus, we monkey-patch in backwards-
# compatibility here so that we don't fill the screen with DeprecationWarnings.

# This no longer seems to be needed pickeshare 0.7.4
# import path
# path.path = path.Path

