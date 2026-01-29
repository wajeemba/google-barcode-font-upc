#!/usr/bin/env python3
"""Examine the working Tall font to understand its metrics."""

from fontTools.ttLib import TTFont

font = TTFont('fonts/LibreBarcode128-Tall.ttf')

# Get metrics
os2 = font['OS/2']
hhea = font['hhea']
head = font['head']
glyf = font['glyf']

print("=== TALL FONT METRICS ===")
print(f"\nOS/2 Metrics:")
print(f"  sTypoAscender: {os2.sTypoAscender}")
print(f"  sTypoDescender: {os2.sTypoDescender}")
print(f"  Line Height: {os2.sTypoAscender - os2.sTypoDescender}")
print(f"  usWinAscent: {os2.usWinAscent}")
print(f"  usWinDescent: {os2.usWinDescent}")

print(f"\nhhea Metrics:")
print(f"  ascent: {hhea.ascent}")
print(f"  descent: {hhea.descent}")
print(f"  lineGap: {hhea.lineGap}")

print(f"\nHead table:")
print(f"  unitsPerEm: {head.unitsPerEm}")
print(f"  xMin: {head.xMin}, xMax: {head.xMax}")
print(f"  yMin: {head.yMin}, yMax: {head.yMax}")

# Find actual glyph bounds
actual_min_y = float('inf')
actual_max_y = float('-inf')
sample_glyphs = []

for glyph_name in font.getGlyphOrder():
    if glyph_name in glyf and glyph_name != '.notdef':
        glyph = glyf[glyph_name]
        if hasattr(glyph, 'yMin') and hasattr(glyph, 'yMax'):
            if glyph.numberOfContours > 0 or (glyph.isComposite() and glyph.numberOfContours == -1):
                actual_min_y = min(actual_min_y, glyph.yMin)
                actual_max_y = max(actual_max_y, glyph.yMax)
                if len(sample_glyphs) < 3 and not glyph_name.startswith('uni'):
                    sample_glyphs.append((glyph_name, glyph.yMin, glyph.yMax))

print(f"\nActual glyph bounds:")
print(f"  Actual yMin: {actual_min_y}")
print(f"  Actual yMax: {actual_max_y}")
print(f"  Actual glyph height: {actual_max_y - actual_min_y}")

print(f"\nSample base glyphs:")
for name, ymin, ymax in sample_glyphs:
    print(f"  {name}: yMin={ymin}, yMax={ymax}, height={ymax-ymin}")

# Calculate proportions
total_height = os2.sTypoAscender - os2.sTypoDescender
ascent_ratio = os2.sTypoAscender / total_height
descent_ratio = abs(os2.sTypoDescender) / total_height

print(f"\nProportions:")
print(f"  Ascent ratio: {ascent_ratio:.4f} ({ascent_ratio*100:.2f}%)")
print(f"  Descent ratio: {descent_ratio:.4f} ({descent_ratio*100:.2f}%)")

# Check fit
print(f"\nFit check:")
print(f"  Glyphs fit in usWinAscent? {actual_max_y} <= {os2.usWinAscent}: {actual_max_y <= os2.usWinAscent}")
print(f"  Glyphs fit in usWinDescent? {abs(actual_min_y)} <= {os2.usWinDescent}: {abs(actual_min_y) <= os2.usWinDescent}")

font.close()
