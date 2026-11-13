"""Long Horizon Observatory documentation theme for Sphinx: Furo with the lab's colors, type and
footer.

Use it with ``html_theme = "lhzn"``. Furo's theme options all still apply; this theme adds
``portal_url`` and ``org_name``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from sphinx.application import Sphinx

__version__ = "0.1.1"

_HERE = Path(__file__).resolve().parent
THEME_DIR = _HERE / "theme" / "lhzn"
STATIC_DIR = THEME_DIR / "static"
# Shared brand files (color tokens, fonts, favicon). An installed wheel carries a copy next to
# this module; a source checkout or editable install reads the repository's tokens/ folder.
TOKENS_DIR = _HERE / "tokens" if (_HERE / "tokens").is_dir() else _HERE.parents[2] / "tokens"


def _builder_inited(app: Sphinx) -> None:
    """Add the shared brand files to the output and fill in the favicon.

    Sphinx loads a theme's module while the HTML builder sets up its templates, after
    config-inited has fired, so both are applied here. The tokens folder goes first in
    html_static_path so a project's own static files can still override a file in it.
    """
    if app.config.html_theme != "lhzn":
        return
    app.config.html_static_path = [str(TOKENS_DIR), *app.config.html_static_path]
    if not app.config.html_favicon:
        app.config.html_favicon = str(TOKENS_DIR / "favicon.svg")


def setup(app: Sphinx) -> dict[str, Any]:
    app.setup_extension("furo")
    app.add_html_theme("lhzn", str(THEME_DIR))
    # Two link tags rather than an @import, so both files get Sphinx's checksum query string and
    # load in parallel.
    app.add_css_file("lhzn-tokens.css", priority=700)
    app.add_css_file("lhzn.css", priority=701)
    app.connect("builder-inited", _builder_inited)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
