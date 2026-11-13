"""Minimal site for checking a built lhzn-sphinx-theme wheel (see publish-sphinx.yml)."""

project = "lhzn-sphinx-theme test site"
author = "Long Horizon Observatory"
html_theme = "lhzn"
html_theme_options = {
    "source_repository": "https://github.com/lhzn-io/lhzn-docs-themes",
    "source_branch": "main",
    "source_directory": "sphinx/tests/site/",
}
