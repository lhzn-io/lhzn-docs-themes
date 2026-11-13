# lhzn-sphinx-theme

The documentation theme for Long Horizon Observatory projects: [Furo](https://github.com/pradyunsg/furo)
with the lab's colors, type, half-moon mark and a footer that links back to the project
documentation portal at [docs.lhzn.io](https://docs.lhzn.io/). Source:
[lhzn-io/lhzn-docs-themes](https://github.com/lhzn-io/lhzn-docs-themes), folder `sphinx/`.

## Use

Add it to `docs/requirements-docs.txt`:

```text
lhzn-sphinx-theme>=0.1,<0.2
```

and in `conf.py`:

```python
html_theme = "lhzn"
html_theme_options = {
    "source_repository": "https://github.com/lhzn-io/<project>",
    "source_branch": "main",
    "source_directory": "docs/source/",
}
```

Remove `sphinx_rtd_theme` from `extensions` and any `.wy-*` rules from the project's `custom.css`;
they target the Read the Docs theme. Every Furo option still works. This theme adds two:

| Option | Default | Purpose |
| :--- | :--- | :--- |
| `portal_url` | `https://docs.lhzn.io/` | Target of the organization label and the footer link; empty hides both. |
| `org_name` | `Long Horizon Observatory` | Text of the organization label and footer link. |

The favicon defaults to the half-moon mark when `html_favicon` is unset. A project logo set with
`html_logo`, or Furo's `light_logo` and `dark_logo`, replaces the mark in the sidebar.

## Modes

Day ("gilded china": eggshell, navy, cobalt) and Night ("chart room": #111111, white, maritime
yellow) follow the reader's system setting until they pick one with Furo's toggle. The values come
from the repository's shared `tokens/lhzn-tokens.css`, which the docs.lhzn.io portal also uses;
this package maps them onto Furo's variables in `theme/lhzn/static/lhzn.css`.

## Fonts

Josefin Sans (headings and labels) is bundled as Latin-subset variable WOFF2 files under the SIL
Open Font License 1.1 (license text in `tokens/fonts/`). Body text and code use the reader's system
sans-serif and monospace faces. Pages make no requests to third-party font or analytics services.

## Releases

Tagged `sphinx-v<version>` in the source repository.

## License

MIT for the theme code; the bundled fonts keep their own license.
