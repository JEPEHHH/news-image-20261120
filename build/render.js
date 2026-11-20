// render.js — screenshot an HTML file with Chromium and report layout metrics
// usage: node render.js <file> <out.png> [width] [height] [scale] [--json]
const { chromium } = require('/root/work/rc/node_modules/playwright-core');
const path = require('path');

(async () => {
  const [file, out, w = '1024', h = '1024', dsf = '1'] = process.argv.slice(2);
  const exe = ['/root/.cache/ms-playwright/chromium-1255/chrome-linux/chrome',
               '/root/.cache/ms-playwright/chromium-1148/chrome-linux/chrome']
              .find(p => require('fs').existsSync(p));
  const browser = await chromium.launch({ executablePath: exe, args: ['--no-sandbox', '--font-render-hinting=none'] });
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +dsf });
  await page.goto('file://' + path.resolve(file), { waitUntil: 'load' });
  await page.waitForTimeout(350);

  // auto-fit: shrink body zoom until the document fits the 1024 canvas
  let zoom = 1;
  for (let i = 0; i < 12; i++) {
    const m = await page.evaluate(() => ({ sh: document.documentElement.scrollHeight, sw: document.documentElement.scrollWidth }));
    if (m.sh <= +h + 1 && m.sw <= +w + 1) break;
    zoom = Math.min(zoom, Math.max(0.80, zoom * ((+h - 2) / m.sh)));
    await page.evaluate(z => { document.body.style.zoom = z; }, zoom);
    await page.waitForTimeout(120);
  }
  const metrics = await page.evaluate(() => {
    const r = el => { const b = el.getBoundingClientRect(); return { top: +b.top.toFixed(1), bottom: +b.bottom.toFixed(1), h: +b.height.toFixed(1) }; };
    const out = {};
    document.querySelectorAll('body > *').forEach((el, i) => { out[(el.className || el.tagName) + '#' + i] = r(el); });
    return { scrollH: document.documentElement.scrollHeight, scrollW: document.documentElement.scrollWidth, blocks: out };
  });
  await page.screenshot({ path: out, clip: { x: 0, y: 0, width: +w, height: +h } });
  console.log(JSON.stringify({ zoom: +zoom.toFixed(3), ...metrics }));
  await browser.close();
})();
