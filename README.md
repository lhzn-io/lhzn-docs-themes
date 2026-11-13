# lhzn-docs-themes

Documentation themes for Long Horizon Observatory projects. The brand values (colors for Day and
Night modes, type, half-moon mark) are defined once in `tokens/`; each documentation tool gets a
small adapter that maps those values onto its own theme variables.

| Folder | Contents | Published as |
| :--- | :--- | :--- |
| `tokens/` | `lhzn-tokens.css`, Josefin Sans (WOFF2, SIL OFL 1.1), `favicon.svg` | copied into each adapter |
| `sphinx/` | Furo child theme, `html_theme = "lhzn"` ([README](sphinx/README.md)) | PyPI `lhzn-sphinx-theme` |

The [docs.lhzn.io](https://docs.lhzn.io/) portal also reads `tokens/` through the Sphinx package.

## Tokens

`lhzn-tokens.css` sets custom properties on `body`: Day ("gilded china": eggshell, navy, cobalt,
gold) by default, Night ("chart room": #111111, white, maritime yellow) under
`body[data-theme=dark]` and under `prefers-color-scheme: dark` when no mode is chosen. An adapter
maps `--lhzn-*` properties onto its tool's variables and does not define colors of its own.

## Adding an adapter

Create a folder named for the tool, with its own build and README, that takes the files from
`tokens/` at build time rather than keeping copies. Add a row to the table above.

## Releases

Each adapter is versioned on its own, with tags prefixed by its folder name: `sphinx-v0.1.0`.

## License

MIT for the theme code (`LICENSE`); the bundled fonts keep their own license
(`tokens/fonts/OFL-JosefinSans.txt`).
