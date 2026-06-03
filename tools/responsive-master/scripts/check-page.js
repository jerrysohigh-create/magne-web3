#!/usr/bin/env node
/**
 * check-page.js — MAGNE.AI Web3 Portal structural validation via Playwright
 *
 * Usage:
 *   node check-page.js <url> [width]
 *   Example: node check-page.js http://127.0.0.1:4174/token.html 1440
 *
 * Outputs: Markdown table to stdout
 * Exit code: 0 = all pass, 1 = one or more fail
 */

const { chromium } = require('playwright');

const VIEWPORTS = [1440, 1320, 1280, 1024, 900, 768, 430, 375, 360];

async function checkPage(url, width) {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width, height: 900 });

  await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });

  const results = {
    width,
    checks: {},
    overall: 'PASS',
  };

  // ── Structural checks ────────────────────────────────────────────────────
  const header = await page.$('.portal-shell-header');
  results.checks.header = header ? 'PASS' : 'FAIL';

  const footer = await page.$('.portal-shell-footer');
  results.checks.footer = footer ? 'PASS' : 'FAIL';

  // Mobile hamburger
  if (width <= 768) {
    const toggle = await page.$('.portal-shell-toggle');
    const isVisible = toggle
      ? await toggle.isVisible()
      : false;
    results.checks.hamburger = isVisible ? 'PASS' : 'FAIL';
  } else {
    results.checks.hamburger = 'N/A';
  }

  // ── Scroll width vs client width ────────────────────────────────────────
  const scrollInfo = await page.evaluate(() => {
    return {
      docScrollW: document.documentElement.scrollWidth,
      docClientW: document.documentElement.clientWidth,
      bodyScrollW: document.body.scrollWidth,
      bodyClientW: document.body.clientWidth,
    };
  });

  const docOk = scrollInfo.docScrollW <= scrollInfo.docClientW;
  const bodyOk = scrollInfo.bodyScrollW <= scrollInfo.bodyClientW;
  results.checks.docOverflow = docOk ? 'PASS' : 'FAIL';
  results.checks.bodyOverflow = bodyOk ? 'PASS' : 'FAIL';
  results.scrollInfo = scrollInfo;

  // ── Check active nav has cyan color ─────────────────────────────────────
  const activeNavColor = await page.evaluate(() => {
    const el = document.querySelector('.portal-shell-nav-link.active');
    if (!el) return 'not found';
    return window.getComputedStyle(el).color;
  });
  results.checks.activeNavColor = activeNavColor;

  // ── Footer social icons ─────────────────────────────────────────────────
  const socialCount = await page.$$eval('.portal-shell-social-link', els => els.length);
  results.checks.footerSocial = socialCount === 4 ? 'PASS' : `FAIL (${socialCount}/4)`;

  // ── Footer legal links ─────────────────────────────────────────────────
  const legalCount = await page.$$eval('.portal-shell-legal-link', els => els.length);
  results.checks.footerLegal = legalCount === 3 ? 'PASS' : `FAIL (${legalCount}/3)`;

  // ── Language menu ───────────────────────────────────────────────────────
  const langOptions = await page.$$eval('.portal-shell-language-option', els => els.length);
  results.checks.langOptions = langOptions >= 2 ? 'PASS' : `FAIL (${langOptions})`;

  await browser.close();

  if (
    results.checks.header === 'FAIL' ||
    results.checks.footer === 'FAIL' ||
    results.checks.docOverflow === 'FAIL' ||
    results.checks.bodyOverflow === 'FAIL'
  ) {
    results.overall = 'FAIL';
  }

  return results;
}

async function main() {
  const url = process.argv[2];
  const specificWidth = process.argv[3] ? parseInt(process.argv[3], 10) : null;

  if (!url) {
    console.error('Usage: node check-page.js <url> [width]');
    console.error('  <url>  — e.g. http://127.0.0.1:4174/token.html');
    console.error('  [width] — optional single viewport; otherwise runs all 9');
    process.exit(1);
  }

  // Check if playwright is available
  try {
    require.resolve('playwright');
  } catch {
    console.error('ERROR: playwright is not installed.');
    console.error('Install with: npm install -g playwright');
    console.error('Then: npx playwright install chromium');
    process.exit(1);
  }

  const targets = specificWidth
    ? [specificWidth]
    : VIEWPORTS;

  console.log(`\n## Responsive Structural Check: ${url}\n`);
  console.log('| Width | Header | Footer | Hamburger | DocOverflow | BodyOverflow | Social | Legal | Overall |');
  console.log('|-------|--------|--------|-----------|-------------|-------------|-------|-------|---------|');

  let hasFail = false;

  for (const w of targets) {
    try {
      const r = await checkPage(url, w);
      if (r.overall === 'FAIL') hasFail = true;
      const { checks } = r;
      console.log(
        `| ${w}px | ${checks.header} | ${checks.footer} | ${checks.hamburger} | ${checks.docOverflow} | ${checks.bodyOverflow} | ${typeof checks.footerSocial === 'string' ? checks.footerSocial : checks.footerSocial} | ${typeof checks.footerLegal === 'string' ? checks.footerLegal : checks.footerLegal} | **${r.overall}** |`
      );
    } catch (err) {
      console.log(`| ${w}px | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | **FAIL** |`);
      console.error(`  Error at ${w}px: ${err.message}`);
      hasFail = true;
    }
  }

  console.log('\n---\n');
  if (hasFail) {
    console.log('**Result: FAIL — one or more viewports failed**\n');
    process.exit(1);
  } else {
    console.log('**Result: PASS — all viewports passed**\n');
    process.exit(0);
  }
}

main().catch(err => {
  console.error('Unhandled error:', err);
  process.exit(1);
});
