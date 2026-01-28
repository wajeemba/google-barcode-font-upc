#!/usr/bin/env python3
"""Examine and debug the VeryTall font to see what's wrong."""

from fontTools.ttLib import TTFont

# Load both fonts to compare
tall_font = TTFont('fonts/LibreBarcode128-Tall.ttf')
verytall_font = TTFont('fonts/LibreBarcode128-VeryTall.ttf')

print("=== TALL FONT ===")
tall_glyf = tall_font['glyf']
tall_os2 = tall_font['OS/2']
tall_head = tall_font['head']

print(f"Ascent: {tall_os2.sTypoAscender}")
print(f"Descent: {tall_os2.sTypoDescender}")
print(f"Bounding box: yMin={tall_head.yMin}, yMax={tall_head.yMax}")

# Check a sample glyph
sample_glyph_name = None
for name in tall_font.getGlyphOrder():
    if name != '.notdef' and name in tall_glyf:
        glyph = tall_glyf[name]
        if glyph.numberOfContours > 0:
            sample_glyph_name = name
            print(f"\nSample glyph '{name}':")
            print(f"  xMin: {glyph.xMin}, xMax: {glyph.xMax}")
            print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
            break

print("\n=== VERY TALL FONT ===")
verytall_glyf = verytall_font['glyf']
verytall_os2 = verytall_font['OS/2']
verytall_head = verytall_font['head']

print(f"Ascent: {verytall_os2.sTypoAscender}")
print(f"Descent: {verytall_os2.sTypoDescender}")
print(f"Bounding box: yMin={verytall_head.yMin}, yMax={verytall_head.yMax}")

if sample_glyph_name:
    glyph = verytall_glyf[sample_glyph_name]
    if glyph.numberOfContours > 0:
        print(f"\nSample glyph '{sample_glyph_name}':")
        print(f"  xMin: {glyph.xMin}, xMax: {glyph.xMax}")
        print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
        print(f"\nGlyph extends beyond ascent? {glyph.yMax > verytall_os2.sTypoAscender}")
        print(f"Glyph extends beyond descent? {glyph.yMin < verytall_os2.sTypoDescender}")

tall_font.close()
verytall_font.close()
