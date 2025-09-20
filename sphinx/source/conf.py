# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bone Physics Docs'
copyright = '2025, zhang0xf'
author = 'zhang0xf'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'
locale_dirs = ['locale/']
gettext_compact = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_context = {
    'languages': {
        'en': {'url': '/en/index.html', 'name': 'English'},
        'zh_CN': {'url': '/zh/index.html', 'name': '简体中文'},
    }
}
