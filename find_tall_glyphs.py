#!/usr/bin/env python3
"""Find all glyphs and their heights in Tall font."""

from fontTools.ttLib import TTFont

tall = TTFont('fonts/LibreBarcode128-Tall.ttf')
glyf = tall['glyf']

glyphs_by_height = []

for glyph_name in tall.getGlyphOrder():
    if glyph_name in glyf:
        glyph = glyf[glyph_name]
        if hasattr(glyph, 'yMax'):
            glyphs_by_height.append((glyph_name, glyph.yMin, glyph.yMax, glyph.yMax - glyph.yMin, glyph.isComposite()))

# Sort by height descending
glyphs_by_height.sort(key=lambda x: x[3], reverse=True)

print("Top 10 tallest glyphs in Tall font:")
for name, ymin, ymax, height, is_composite in glyphs_by_height[:10]:
    comp_str = " (composite)" if is_composite else ""
    print(f"  {name}: yMin={ymin}, yMax={ymax}, height={height}{comp_str}")

tall.close()
