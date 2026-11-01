"""
Screen and Active Window Context Capture Module.
Captures screen frames and extracts visual/textual context for prompt generation.
"""

import time
import os
import mss
from PIL import Image
import imagehash


def capture_screen(output_path: str = None) -> Image.Image:
    """
    Captures the primary monitor screen.
    Optionally saves the image to `output_path`.
    """
    try:
        with mss.MSS() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            if output_path:
                img.save(output_path)
            return img
    except Exception as e:
        print(f"[Warning] Screen capture failed: {e}")
        return None


def get_image_hash(image: Image.Image) -> str:
    """Computes a perceptual difference hash (dhash) to identify visual changes."""
    if image is None:
        return ""
    return str(imagehash.dhash(image))


if __name__ == "__main__":
    print("Testing screen capture module...")
    img = capture_screen()
    if img:
        img_hash = get_image_hash(img)
        print(f"Captured screen size: {img.size}, Hash: {img_hash}")
    else:
        print("Screen capture skipped (no active display session or permission).")
