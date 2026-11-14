#!/usr/bin/env python3
import os
import glob
import shutil

BRAIN_DIR = "/Users/bhavishlakkavarapu/.gemini/antigravity/brain/2d4ff547-b2a5-4f59-9874-6e440d8929d4"
WORKSPACE_DIR = "/Users/bhavishlakkavarapu/Downloads/physic readings "

MAPPING = {
    ("tarot_hero", "tarot-hero"): ("tarot-reading", "hero.jpg", "sanctuary-reading-table.jpg"),
    ("tarot_content", "tarot-content"): ("tarot-reading", "content.jpg", "sanctuary-crystal-altar.jpg"),
    ("psychic_hero", "psychic-hero"): ("psychic-reading", "hero.jpg", "sanctuary-reading-table.jpg"),
    ("psychic_content", "psychic-content"): ("psychic-reading", "content.jpg", "sanctuary-palmistry-neon.jpg"),
    ("medium_hero", "medium-hero"): ("medium-reading", "hero.jpg", "sanctuary-crystal-altar.jpg"),
    ("medium_content", "medium-content"): ("medium-reading", "content.jpg", "sanctuary-chakras-room.jpg"),
    ("reiki_hero", "reiki-hero"): ("energy-healing", "hero.jpg", "sanctuary-chakras-room.jpg"),
    ("reiki_content", "reiki-content"): ("energy-healing", "content.jpg", "sanctuary-crystal-altar.jpg"),
    ("chakra_hero", "chakra-hero"): ("chakra-balancing", "hero.jpg", "sanctuary-chakras-room.jpg"),
    ("chakra_content", "chakra-content"): ("chakra-balancing", "content.jpg", "sanctuary-chakras-room.jpg"),
    ("holistic_hero", "holistic-hero"): ("holistic-counseling", "hero.jpg", "sanctuary-reading-table.jpg"),
    ("holistic_content", "holistic-content"): ("holistic-counseling", "content.jpg", "sanctuary-crystal-altar.jpg"),
    ("meditation_hero", "meditation-hero"): ("meditation", "hero.jpg", "sanctuary-chakras-room.jpg"),
    ("meditation_content", "meditation-content"): ("meditation", "content.jpg", "sanctuary-crystal-altar.jpg"),
}

def sync():
    print("Syncing service images...")
    for prefixes, (serv_dir, dest_file, fallback) in MAPPING.items():
        dest_dir = os.path.join(WORKSPACE_DIR, "assets", "images", "services", serv_dir)
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, dest_file)
        
        # Look for matching files in BRAIN_DIR
        matched_files = []
        for prefix in prefixes:
            pattern = os.path.join(BRAIN_DIR, f"{prefix}*.*")
            matched_files.extend(glob.glob(pattern))
            
        if matched_files:
            # Sort by mtime descending
            matched_files.sort(key=os.path.getmtime, reverse=True)
            src_file = matched_files[0]
            shutil.copy2(src_file, dest_path)
            print(f"[GENERATED] {os.path.basename(src_file)} -> {serv_dir}/{dest_file} ({os.path.getsize(dest_path)} bytes)")
        else:
            # Use authentic fallback if not yet generated
            if not os.path.exists(dest_path):
                fallback_path = os.path.join(WORKSPACE_DIR, "assets", "images", fallback)
                if os.path.exists(fallback_path):
                    shutil.copy2(fallback_path, dest_path)
                    print(f"[FALLBACK] {fallback} -> {serv_dir}/{dest_file}")
                else:
                    print(f"[MISSING] {serv_dir}/{dest_file}")
            else:
                print(f"[EXISTS] {serv_dir}/{dest_file}")

if __name__ == "__main__":
    sync()
