#!/usr/bin/env python3
"""Verify Very Tall font matches Tall proportions."""

from fontTools.ttLib import TTFont

print("=== COMPARING TALL AND VERY TALL ===\n")

# Load Tall font
tall = TTFont('fonts/LibreBarcode128-Tall.ttf')
tall_os2 = tall['OS/2']
tall_glyf = tall['glyf']

# Find Tall glyph height
tall_max_y = 0
for glyph_name in tall.getGlyphOrder():
    if glyph_name in tall_glyf and not glyph_name.startswith('uni') and glyph_name != '.notdef':
        glyph = tall_glyf[glyph_name]
        if hasattr(glyph, 'yMax') and glyph.numberOfContours > 0:
            tall_max_y = max(tall_max_y, glyph.yMax)
            if tall_max_y > 0:
                break

print("TALL FONT:")
print(f"  Ascent: {tall_os2.sTypoAscender}")
print(f"  Descent: {tall_os2.sTypoDescender}")
print(f"  Total: {tall_os2.sTypoAscender - tall_os2.sTypoDescender}")
print(f"  Glyph height: {tall_max_y}")
print(f"  Ascent %: {tall_os2.sTypoAscender / (tall_os2.sTypoAscender - tall_os2.sTypoDescender) * 100:.2f}%")
print(f"  Descent %: {abs(tall_os2.sTypoDescender) / (tall_os2.sTypoAscender - tall_os2.sTypoDescender) * 100:.2f}%")
print(f"  Glyph fits in ascent? {tall_max_y <= tall_os2.usWinAscent}")

tall.close()

# Load Very Tall font
verytall = TTFont('fonts/LibreBarcode128-VeryTall.ttf')
verytall_os2 = verytall['OS/2']
verytall_glyf = verytall['glyf']

# Find Very Tall glyph height
verytall_max_y = 0
for glyph_name in verytall.getGlyphOrder():
    if glyph_name in verytall_glyf and not glyph_name.startswith('uni') and glyph_name != '.notdef':
        glyph = verytall_glyf[glyph_name]
        if hasattr(glyph, 'yMax') and glyph.numberOfContours > 0:
            verytall_max_y = max(verytall_max_y, glyph.yMax)
            if verytall_max_y > 0:
                break

print("\nVERY TALL FONT:")
print(f"  Ascent: {verytall_os2.sTypoAscender}")
print(f"  Descent: {verytall_os2.sTypoDescender}")
print(f"  Total: {verytall_os2.sTypoAscender - verytall_os2.sTypoDescender}")
print(f"  Glyph height: {verytall_max_y}")
print(f"  Ascent %: {verytall_os2.sTypoAscender / (verytall_os2.sTypoAscender - verytall_os2.sTypoDescender) * 100:.2f}%")
print(f"  Descent %: {abs(verytall_os2.sTypoDescender) / (verytall_os2.sTypoAscender - verytall_os2.sTypoDescender) * 100:.2f}%")
print(f"  Glyph fits in ascent? {verytall_max_y <= verytall_os2.usWinAscent}")

verytall.close()

print("\nCOMPARISON:")
tall_total = tall_os2.sTypoAscender - tall_os2.sTypoDescender
verytall_total = verytall_os2.sTypoAscender - verytall_os2.sTypoDescender
print(f"  Very Tall / Tall total height: {verytall_total / tall_total:.2f}x")
print(f"  Very Tall / Tall glyph height: {verytall_max_y / tall_max_y:.2f}x")
print(f"  Proportions match? {abs((verytall_os2.sTypoAscender / verytall_total) - (tall_os2.sTypoAscender / tall_total)) < 0.001}")
