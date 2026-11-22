// Render PNG and ICO exports from the optimized SVGs.
// Run from design/brand/:  node export-png.js   (needs Playwright with Chromium)
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const svgDir = path.join(__dirname, "svg");
const outDir = path.join(__dirname, "png");
fs.mkdirSync(outDir, { recursive: true });
// Inline the SVG so nothing loads over file://.
const inline = (f, w) =>
  `<div style="width:${w}px">${fs.readFileSync(path.join(svgDir, f), "utf8")}</div>`;

// [file, size or [w,h], html]
const jobs = [
  ["favicon-16.png", 16, inline("favicon.svg", 16)],
  ["favicon-32.png", 32, inline("favicon.svg", 32)],
  ["favicon-48.png", 48, inline("favicon.svg", 48)],
  ["icon-512.png", 512, inline("mark-tile.svg", 512)],
  // iOS rounds the corners itself, so this one is a full-bleed square.
  ["apple-touch-icon.png", 180,
    `<div style="width:180px;height:180px;background:#0B2540;display:grid;place-items:center">${inline("mark-reverse.svg", 120)}</div>`],
  ["og-image.png", [1200, 630], inline("og-image.svg", 1200)],
  ["lockup-1200.png", [1200, null], inline("lockup.svg", 1200)],
];

(async () => {
  const browser = await chromium.launch();
  for (const [file, size, html] of jobs) {
    const [w, h] = Array.isArray(size) ? size : [size, size];
    const page = await browser.newPage({ viewport: { width: w, height: h || 600 }, deviceScaleFactor: 1 });
    await page.setContent(`<style>html,body{margin:0;background:transparent}svg{display:block;width:100%;height:auto}</style>${html}`);
    await page.waitForLoadState("load");
    const el = await page.$("body > *");
    await el.screenshot({ path: path.join(outDir, file), omitBackground: true });
    await page.close();
  }
  await browser.close();
})();
