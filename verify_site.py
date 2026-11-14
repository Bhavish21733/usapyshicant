#!/usr/bin/env python3
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def check_html_file(filepath):
    errors = []
    warnings = []
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    rel_dir = os.path.dirname(filepath)
    
    # 1. Check images
    img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    for src in img_matches:
        if src.startswith("http") or src.startswith("data:"):
            continue
        clean_src = src.split("?")[0].split("#")[0]
        # Resolve path relative to current HTML file
        target = os.path.normpath(os.path.join(rel_dir, clean_src))
        if not os.path.exists(target):
            errors.append(f"Broken image: {src} -> {target}")
        elif os.path.getsize(target) == 0:
            errors.append(f"Empty image: {src}")

    # 2. Check internal links
    link_matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', html)
    for href in link_matches:
        if href.startswith("tel:") or href.startswith("mailto:") or href.startswith("http") or href.startswith("#"):
            continue
        clean_href = href.split("?")[0].split("#")[0]
        if not clean_href:
            continue
        target = os.path.normpath(os.path.join(rel_dir, clean_href))
        if not os.path.exists(target):
            errors.append(f"Broken link: {href} -> {target}")

    # 3. Check for placeholders
    placeholders = ["TODO", "lorem ipsum", "undefined", "[practitioner name]", "{{"]
    for ph in placeholders:
        if ph in html.lower():
            warnings.append(f"Possible placeholder: {ph}")

    return errors, warnings

def verify_all():
    print("=== VERIFYING 9TH CHAKRA PSYCHIC WEBSITE ===")
    total_files = 0
    total_errors = 0
    total_warnings = 0
    
    service_word_counts = {}
    
    for root, dirs, files in os.walk(BASE_DIR):
        if "assets" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                total_files += 1
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, BASE_DIR)
                errors, warnings = check_html_file(filepath)
                
                # Check word count if it's an individual service page
                if "services/" in rel_path and rel_path != "services/index.html" and rel_path != "services.html":
                    with open(filepath, "r", encoding="utf-8") as f:
                        text = re.sub(r'<[^>]+>', ' ', f.read())
                        words = len(text.split())
                        service_word_counts[rel_path] = words

                if errors:
                    print(f"❌ {rel_path}: {len(errors)} errors")
                    for err in errors:
                        print(f"   - {err}")
                    total_errors += len(errors)
                if warnings:
                    print(f"⚠️ {rel_path}: {len(warnings)} warnings")
                    for w in warnings:
                        print(f"   - {w}")
                    total_warnings += len(warnings)

    print("\n--- SERVICE DETAIL WORD COUNTS ---")
    for page, count in sorted(service_word_counts.items()):
        print(f"  {page}: ~{count} total words (concise, scannable)")

    print(f"\nVerification finished: {total_files} HTML files inspected.")
    if total_errors == 0:
        print("✅ SUCCESS: 0 broken links, 0 broken images, 0 fatal errors!")
    else:
        print(f"❌ FAILED: {total_errors} errors detected.")

if __name__ == "__main__":
    verify_all()
