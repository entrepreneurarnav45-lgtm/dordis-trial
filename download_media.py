#!/usr/bin/env python3
"""
Downloads the clinic's images and video into the images/ folder next to this file.
index.html already points at these local files, so after running this the
whole folder works offline (except Google Fonts and the Google Map).

    python download_media.py
"""
import urllib.request
from pathlib import Path

BASE = "https://radiant-smiles-intro.lovable.app/__l5e/assets-v1/"
FILES = {
    "logo.png":           "e0ec9991-5d08-450b-899e-1791cf6a4dc8/logo.png",
    "dr-jehan-dordi.jpg": "d8f5cd8e-00d8-4314-aa80-bfde43e19b39/dr-jehan-dordi.jpg",
    "smile-before.jpg":   "425dfe8f-3f24-4a67-9ed2-0c8497f4e985/smile-before.jpg",
    "smile-after.jpg":    "4c2e1ec8-36ad-44c0-9856-a26f0a41723a/smile-after.jpg",
    "inside-clinic.mp4":  "227adea5-45b4-4398-8efb-883b2c82142c/inside-clinic.mp4",
}

out = Path(__file__).resolve().parent / "images"
out.mkdir(exist_ok=True)

failed = 0
for name, path in FILES.items():
    dest = out / name
    print(f"Downloading {name} ...", end=" ", flush=True)
    try:
        req = urllib.request.Request(BASE + path, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            dest.write_bytes(r.read())
        print(f"{dest.stat().st_size / 1024:.0f} KB")
    except Exception as e:  # noqa: BLE001
        failed += 1
        print(f"FAILED ({e})")

print("\nAll files saved in", out if not failed else f"{out} ({failed} failed, run again)")
