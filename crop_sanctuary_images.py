#!/usr/bin/env python3
import os
from PIL import Image

WORKSPACE_DIR = "/Users/bhavishlakkavarapu/Downloads/physic readings "
IMG_DIR = os.path.join(WORKSPACE_DIR, "assets", "images")

# The 4 sanctuary images are 768 x 1024 portrait with drop ceilings at the top
def crop_images():
    print("Cropping sanctuary images to remove ceiling and focus on sanctuary...")
    
    # 1. Reading table: crop ceiling (y: 160 -> 940) -> 768 x 780
    p1 = os.path.join(IMG_DIR, "sanctuary-reading-table.jpg")
    if os.path.exists(p1):
        with Image.open(p1) as im:
            # Crop to focus on the crystal ball, mirror, gold hand, and zodiac rug
            box = (0, 140, im.width, 920)
            cropped = im.crop(box)
            out_path = os.path.join(IMG_DIR, "sanctuary-reading-table-crop.jpg")
            cropped.save(out_path, "JPEG", quality=92)
            print(f"Saved: {out_path} ({cropped.size})")

    # 2. Chakras room: crop top ceiling light (y: 180 -> 900)
    p2 = os.path.join(IMG_DIR, "sanctuary-chakras-room.jpg")
    if os.path.exists(p2):
        with Image.open(p2) as im:
            box = (0, 160, im.width, 880)
            cropped = im.crop(box)
            out_path = os.path.join(IMG_DIR, "sanctuary-chakras-room-crop.jpg")
            cropped.save(out_path, "JPEG", quality=92)
            print(f"Saved: {out_path} ({cropped.size})")

    # 3. Palmistry neon: crop top ceiling (y: 120 -> 920)
    p3 = os.path.join(IMG_DIR, "sanctuary-palmistry-neon.jpg")
    if os.path.exists(p3):
        with Image.open(p3) as im:
            box = (0, 120, im.width, 900)
            cropped = im.crop(box)
            out_path = os.path.join(IMG_DIR, "sanctuary-palmistry-neon-crop.jpg")
            cropped.save(out_path, "JPEG", quality=92)
            print(f"Saved: {out_path} ({cropped.size})")

    # 4. Crystal altar: crop top ceiling (y: 150 -> 900)
    p4 = os.path.join(IMG_DIR, "sanctuary-crystal-altar.jpg")
    if os.path.exists(p4):
        with Image.open(p4) as im:
            box = (0, 150, im.width, 900)
            cropped = im.crop(box)
            out_path = os.path.join(IMG_DIR, "sanctuary-crystal-altar-crop.jpg")
            cropped.save(out_path, "JPEG", quality=92)
            print(f"Saved: {out_path} ({cropped.size})")

if __name__ == "__main__":
    crop_images()
