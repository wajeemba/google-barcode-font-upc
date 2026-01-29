#!/usr/bin/env python3
"""
Modify the LibreBarcode 128 font for even taller display.

Creates a "Very Tall" version that's 1.65x the height of the Tall variant.
Uses the same ascender/descender proportions as the Tall variant.
Builds from the Tall font to preserve composite glyph structure.
"""

from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform
import os

# Load the TALL font as input (not the original)
# This preserves the composite glyph structure with proper transforms
input_font = 'fonts/LibreBarcode128-Tall.ttf'
output_font = 'fonts/LibreBarcode128-VeryTall.ttf'

print(f"Loading font: {input_font}")
font = TTFont(input_font)

# Get Tall font metrics
head = font['head']
os2 = font['OS/2']
hhea = font['hhea']

tall_ascent = os2.sTypoAscender  # 1100
tall_descent = os2.sTypoDescender  # -1000
tall_total = tall_ascent + abs(tall_descent)  # 2100

print(f"\nTall font metrics:")
print(f"  Ascent: {tall_ascent}")
print(f"  Descent: {tall_descent}")
print(f"  Total height: {tall_total}")

# Calculate Very Tall metrics
# Very Tall should be 1.65x of Tall
very_tall_multiplier = 1.65
new_total = int(tall_total * very_tall_multiplier)  # 3465

# Use same proportions as Tall
ascent_ratio = tall_ascent / tall_total  # 0.5238
descent_ratio = abs(tall_descent) / tall_total  # 0.4762

new_ascent = int(new_total * ascent_ratio)  # 1815
new_descent = -int(new_total * descent_ratio)  # -1650

# Calculate glyph scale factor
# Just scale the Tall glyphs by 1.65x
scale_factor = very_tall_multiplier  # 1.65x

print(f"\nNew metrics (Very Tall - {very_tall_multiplier}x of Tall):")
print(f"  Ascent: {new_ascent}")
print(f"  Descent: {new_descent}")
print(f"  Total height: {new_total}")
print(f"  Glyph scale factor: {scale_factor}x (from Tall)")
print(f"  Expected base glyph height: ~{int(885 * scale_factor)}")
print(f"  Expected composite height: ~{int(1328 * scale_factor)}")

# Get the glyph set
glyf_table = font['glyf']
hmtx_table = font['hmtx']

print(f"\nScaling glyphs by {scale_factor}x vertically...")

glyph_set = font.getGlyphSet()
glyph_names = font.getGlyphOrder()

for glyph_name in glyph_names:
    if glyph_name == '.notdef' or glyph_name not in glyf_table:
        continue

    glyph = glyf_table[glyph_name]

    # Skip composite glyphs - they reference other glyphs and will be scaled automatically
    if glyph.isComposite():
        continue

    # Skip empty glyphs
    if glyph.numberOfContours == 0:
        continue

    # Create a transformation matrix for vertical scaling
    transform = Transform(1, 0, 0, scale_factor, 0, 0)

    # Create a new glyph pen
    tt_pen = TTGlyphPen(font.getGlyphSet())

    # Draw the glyph with transformation
    transform_pen = TransformPen(tt_pen, transform)

    # Draw the original glyph through the transform
    glyph_set[glyph_name].draw(transform_pen)

    # Replace the glyph
    new_glyph = tt_pen.glyph()
    glyf_table[glyph_name] = new_glyph

# Recalculate bounds for all glyphs
print("\nRecalculating glyph bounds...")
for glyph_name in glyph_names:
    if glyph_name in glyf_table:
        glyph = glyf_table[glyph_name]
        if hasattr(glyph, 'recalcBounds'):
            glyph.recalcBounds(glyf_table)

# Update font metrics in OS/2 table
os2.sTypoAscender = new_ascent
os2.sTypoDescender = new_descent
os2.usWinAscent = new_ascent
os2.usWinDescent = abs(new_descent)

# Update hhea table
hhea.ascent = new_ascent
hhea.descent = new_descent

# Manually recalculate bounding box from actual glyphs
print("\nRecalculating bounding box from glyphs...")
min_y = 0
max_y = 0
for glyph_name in glyph_names:
    if glyph_name in glyf_table:
        glyph = glyf_table[glyph_name]
        if hasattr(glyph, 'yMin') and hasattr(glyph, 'yMax'):
            if glyph.yMin < min_y:
                min_y = glyph.yMin
            if glyph.yMax > max_y:
                max_y = glyph.yMax

head.yMin = min_y
head.yMax = max_y
print(f"Calculated bounding box: yMin={min_y}, yMax={max_y}")

# Update font name to indicate it's Very Tall
name_table = font['name']
for record in name_table.names:
    if record.nameID == 1:  # Font Family name
        record.string = "Libre Barcode 128 Very Tall"
    elif record.nameID == 4:  # Full font name
        record.string = "Libre Barcode 128 Very Tall Regular"
    elif record.nameID == 6:  # PostScript name
        record.string = "LibreBarcode128-VeryTall"

print(f"\nSaving modified font: {output_font}")
font.save(output_font)
font.close()

print(f"✓ Font modification complete!")
print(f"  Original: {input_font}")
print(f"  Very Tall: {output_font}")
