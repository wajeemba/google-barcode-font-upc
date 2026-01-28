#!/usr/bin/env python3
"""Find the glyph with bad bounds."""

from fontTools.ttLib import TTFont

font = TTFont('fonts/LibreBarcode128-VeryTall.ttf')
glyf = font['glyf']

print("Glyphs with yMax > 2000:")
for glyph_name in font.getGlyphOrder():
    if glyph_name in glyf:
        glyph = glyf[glyph_name]
        if hasattr(glyph, 'yMax') and glyph.yMax > 2000:
            print(f"  {glyph_name}: yMin={glyph.yMin}, yMax={glyph.yMax}, contours={glyph.numberOfContours}")
            if glyph.isComposite():
                print(f"    (composite glyph)")

font.close()
