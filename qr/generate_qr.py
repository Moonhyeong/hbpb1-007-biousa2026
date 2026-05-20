"""Generate BIO USA 2026 QR code for HBPB1-007 partnering landing page.

- Target URL: https://moonhyeong.github.io/hbpb1-007-biousa2026/
- Foreground: Navy #1E2761 (matches landing page primary color)
- Error correction: H (30%) to tolerate print damage, folding, partial occlusion
- Output: ~2000 px PNG (300 dpi at ~10 cm; safe for any print size from 2.5 cm up)
- Also produces SVG for lossless scaling
"""
import qrcode
from qrcode.image.svg import SvgPathImage

URL = "https://moonhyeong.github.io/hbpb1-007-biousa2026/"
NAVY_RGB = (30, 39, 97)     # #1E2761 — landing page primary color
OUT_PNG = "qr_hbpb1-007-biousa2026_navy.png"
OUT_SVG = "qr_hbpb1-007-biousa2026_navy.svg"

# Build QR with high error correction and explicit box size for ~2000 px output
qr = qrcode.QRCode(
    version=None,                       # auto-fit version based on data length
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=40,                        # px per module
    border=4,                           # quiet zone (modules)
)
qr.add_data(URL)
qr.make(fit=True)

# --- PNG (default PilImage respects RGB tuples) ---
img = qr.make_image(fill_color=NAVY_RGB, back_color="white")
img = img.convert("RGB")
img.save(OUT_PNG)

# --- SVG ---
svg_img = qr.make_image(image_factory=SvgPathImage, fill_color="#1E2761", back_color="white")
svg_img.save(OUT_SVG)

print(f"QR version: {qr.version} · modules: {qr.modules_count} · ECC: H")
print(f"PNG saved: {OUT_PNG}")
print(f"SVG saved: {OUT_SVG}")
print(f"URL encoded: {URL}")
