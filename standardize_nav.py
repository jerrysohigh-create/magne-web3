#!/usr/bin/env python3
"""
Standardize mobile hamburger menu across all TC pages using token.html as template.
Only syncs: nav HTML, mobile-menu HTML, CSS, JS, and active states.
"""

import re
from pathlib import Path

TC_DIR = Path("/home/gaojie20/.openclaw/workspace-main/magne-web3/tc")
TOKEN_FILE = TC_DIR / "token.html"

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def set_active_link(html, active_text, is_mobile=False):
    """Set the active class on the correct nav link"""
    html = re.sub(r'(<a href="[^"]+") class="active"', r'\1', html)
    pattern = r'(<a href="[^"]+")>' + re.escape(active_text) + r'(<\/a>)'
    replacement = r'\1 class="active">' + active_text + r'\2'
    html = re.sub(pattern, replacement, html)
    return html

def extract_canonical(token_html):
    """Extract canonical sections from token.html"""
    
    # Extract style block
    style_match = re.search(r'<style>(.*?)</style>', token_html, re.DOTALL)
    if not style_match:
        print("ERROR: Could not find style block in token.html")
        return None
    
    css_content = style_match.group(1)
    lines = css_content.split('\n')
    
    # Extract canonical nav CSS (all lines that start with nav or .nav or .mobile or footer)
    nav_css_lines = []
    for line in lines:
        stripped = line.strip()
        if (stripped.startswith('nav') or 
            stripped.startswith('.nav') or 
            stripped.startswith('.mobile-menu') or
            stripped.startswith('.container') or
            'footer' in stripped.lower() or
            '@media' in stripped):
            nav_css_lines.append(line)
    
    # Extract nav HTML
    nav_match = re.search(r'(  <nav>[\s\S]*?<\/nav>\n)', token_html)
    nav_html = nav_match.group(1) if nav_match else ""
    
    # Extract mobile menu HTML (full div with nested content)
    mobile_match = re.search(r'(  <div class="mobile-menu"[^>]*>[\s\S]*?<\/div>\n)', token_html)
    mobile_html = mobile_match.group(1) if mobile_match else ""
    
    # Extract mobile menu JS
    js_match = re.search(r'(<script>[\s\S]*?const mobileMenuBtn[\s\S]*?<\/script>)', token_html)
    mobile_js = js_match.group(1) if js_match else ""
    
    return {
        'css': '\n'.join(nav_css_lines),
        'nav_html': nav_html,
        'mobile_html': mobile_html,
        'js': mobile_js,
    }

def process_page(page_path, canonical, active_text):
    """Process a single page to standardize nav/mobile-menu"""
    
    page_html = read_file(page_path)
    
    # Check if page has nav element
    if '<nav>' not in page_html and '<nav ' not in page_html:
        print(f"  SKIP: {page_path.name} - no nav element found")
        return False
    
    print(f"  Processing: {page_path.name}")
    
    # Replace nav HTML
    nav_pattern = r'  <nav>[\s\S]*?<\/nav>\n'
    nav_match = re.search(nav_pattern, page_html)
    if nav_match:
        canonical_nav = set_active_link(canonical['nav_html'], active_text, is_mobile=False)
        page_html = page_html.replace(nav_match.group(0), canonical_nav)
    
    # Replace mobile menu HTML
    # The mobile-menu div contains nested divs, so we need to match carefully
    # Strategy: find <div class="mobile-menu"...> and replace until the matching </div>
    # We do this by finding the opening, then counting braces to find the closing
    
    canonical_mobile = set_active_link(canonical['mobile_html'], active_text, is_mobile=True)
    
    # Try to find and replace the full mobile-menu div
    mobile_start = re.search(r'\s*<div class="mobile-menu"[^>]*>', page_html)
    if mobile_start:
        # Find the end of the mobile-menu div by counting nested divs
        search_from = mobile_start.end()
        div_count = 1  # Already found one opening div
        pos = search_from
        while div_count > 0 and pos < len(page_html):
            # Look for next opening or closing div
            next_open = page_html.find('<div', pos)
            next_close = page_html.find('</div>', pos)
            
            if next_close == -1:
                break
            if next_open == -1 or next_close < next_open:
                # Closing div comes first
                div_count -= 1
                pos = next_close + 6  # len('</div>')
            else:
                # Opening div comes first
                div_count += 1
                pos = next_open + 4
        
        if div_count == 0:
            # Found the matching closing div
            end_pos = pos
            old_mobile_html = page_html[mobile_start.start():end_pos]
            page_html = page_html[:mobile_start.start()] + canonical_mobile + page_html[end_pos:]
        else:
            # Couldn't find matching close, just insert after </nav>
            print(f"    WARNING: Could not find proper mobile-menu closing tag in {page_path.name}")
            page_html = re.sub(r'(</nav>\n)', r'\1\n' + canonical_mobile, page_html, count=1)
    else:
        # No mobile-menu div found, insert after </nav>
        print(f"    INFO: No mobile-menu div found in {page_path.name}, inserting...")
        page_html = re.sub(r'(</nav>\n)', r'\1\n' + canonical_mobile, page_html, count=1)
    
    # Replace mobile menu JS
    js_pattern = r'<script>[\s\S]*?const mobileMenuBtn[\s\S]*?<\/script>'
    js_match = re.search(js_pattern, page_html)
    if js_match:
        page_html = page_html.replace(js_match.group(0), canonical['js'])
    
    # Insert canonical CSS at the beginning of style block
    style_match = re.search(r'(<style>)([\s\S]*?)(</style>)', page_html)
    if style_match:
        existing_css = style_match.group(2)
        canonical_css = '\n    /* === CANONICAL NAV/MENU CSS === */\n' + canonical['css'] + '\n'
        new_css = existing_css + '\n' + canonical_css
        new_style = style_match.group(1) + new_css + style_match.group(3)
        page_html = page_html.replace(style_match.group(0), new_style)
    
    write_file(page_path, page_html)
    return True

def main():
    print("Reading canonical template (token.html)...")
    token_html = read_file(TOKEN_FILE)
    
    canonical = extract_canonical(token_html)
    if not canonical:
        return
    
    print(f"  Extracted CSS, nav HTML, mobile menu HTML, and JS")
    
    # Process main pages with nav
    main_pages = [
        ("index.html", "首頁"),
        ("agent-pay.html", "AGENT PAY"),
        ("network.html", "網絡"),
        ("developers.html", "開發者"),
        ("ecosystem.html", "生態"),
        ("transparency.html", "透明中心"),
        ("faq.html", "常見問題"),
    ]
    
    print("\nProcessing main TC pages...")
    for page_rel, active_text in main_pages:
        page_path = TC_DIR / page_rel
        if page_path.exists():
            process_page(page_path, canonical, active_text)
        else:
            print(f"  SKIP: {page_rel} - file not found")
    
    # Process additional pages
    additional_pages = [
        ("learn.html", "首頁"),
        ("evidence.html", "透明中心"),
        ("developers-agent-pay.html", "開發者"),
        ("developers-app.html", "開發者"),
        ("developers-connect.html", "開發者"),
        ("developers-contract.html", "開發者"),
        ("tokenomics-detail.html", "代幣"),
        ("token-status.html", "代幣"),
        ("version-history.html", "透明中心"),
        ("session2.html", "網絡"),
    ]
    
    print("\nProcessing additional TC pages...")
    for page_rel, active_text in additional_pages:
        page_path = TC_DIR / page_rel
        if page_path.exists():
            page_html = read_file(page_path)
            if '<nav>' in page_html or '<nav ' in page_html:
                process_page(page_path, canonical, active_text)
            else:
                print(f"  SKIP: {page_rel} - no nav element")
        else:
            print(f"  SKIP: {page_rel} - file not found")
    
    print("\nDone!")

if __name__ == "__main__":
    main()
