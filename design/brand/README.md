# Electric Dev logo and branding

Open `index.html` in a browser to see the mark, lockups, color versions, rules and exports.

Everything uses the Pacific Current style guide's colors and fonts (Source Serif 4 and
IBM Plex Sans, weights 400 and 600). The SVGs are hand-coded; the wordmark is set from
the fonts in `fonts/` and converted to outlines, so no SVG needs a web font.

## Rebuild (for example, if the name changes)

Edit `NAME` and `DOMAIN` at the top of `build.py`, then from this folder:

```bash
python3 -m pip install fonttools brotli uharfbuzz   # once
python3 build.py                                     # writes svg/
npx svgo@3 --config svgo.config.mjs -f svg -o svg    # optimizes in place
node export-png.js                                   # writes png/ (needs Playwright)
python3 -c "from PIL import Image; i=[Image.open(f'png/favicon-{s}.png') for s in (16,32,48)]; i[2].save('png/favicon.ico', sizes=[(16,16),(32,32),(48,48)], append_images=i[:2])"
```

## Folders

- `svg/` optimized SVGs (lockups, mark, favicon, share card, two unchosen concepts)
- `png/` raster exports (favicons, app icons, share card, a 1200px lockup)
- `fonts/` copies of the style guide's fonts, for this page and the build
