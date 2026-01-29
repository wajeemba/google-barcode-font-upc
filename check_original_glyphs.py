#!/usr/bin/env python3
"""Check original font glyph heights."""

from fontTools.ttLib import TTFont

font = TTFont('fonts/LibreBarcode128-Regular.ttf')
glyf = font['glyf']

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

print(f"Original font actual glyph bounds:")
print(f"  Actual yMin: {actual_min_y}")
print(f"  Actual yMax: {actual_max_y}")
print(f"  Actual glyph height: {actual_max_y - actual_min_y}")

print(f"\nSample base glyphs:")
for name, ymin, ymax in sample_glyphs:
    print(f"  {name}: yMin={ymin}, yMax={ymax}, height={ymax-ymin}")

# Now calculate what scale factor was used for Tall
tall_glyph_max = 1328
original_glyph_max = actual_max_y
scale = tall_glyph_max / original_glyph_max

print(f"\nScale factor (Tall glyph max / Original glyph max):")
print(f"  {tall_glyph_max} / {original_glyph_max} = {scale:.4f}x")

font.close()
