#!/usr/bin/env python3
"""
Modify the LibreBarcode 128 font for even taller display.

Creates a "Very Tall" version that's twice the height of the Tall variant.
Keeps the descender the same and adds all extra height above.
"""

from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform
import os

# Load the font
input_font = 'fonts/LibreBarcode128-Regular.ttf'
output_font = 'fonts/LibreBarcode128-VeryTall.ttf'

print(f"Loading font: {input_font}")
font = TTFont(input_font)

# Get current metrics
head = font['head']
os2 = font['OS/2']
hhea = font['hhea']

current_ascent = os2.sTypoAscender  # 600
current_descent = os2.sTypoDescender  # -400
current_total = current_ascent + abs(current_descent)  # 1000

print(f"\nOriginal metrics:")
print(f"  Ascent: {current_ascent}")
print(f"  Descent: {current_descent}")
print(f"  Total height: {current_total}")

# Calculate new metrics for Very Tall version
# Tall version has: Ascent 1100, Descent -1000, Total 2100
# Very Tall should be 2x of Tall = 4200 total
# Keep descent at -1000 (same as Tall)
# Add all extra height to ascent

new_descent = -1000  # Same as Tall version
new_total = 4200  # 2x of Tall version (2100 * 2)
new_ascent = new_total - abs(new_descent)  # 3200

print(f"\nNew metrics (Very Tall):")
print(f"  Ascent: {new_ascent}")
print(f"  Descent: {new_descent}")
print(f"  Total height: {new_total}")
print(f"  Height vs Original: {new_total/current_total:.1f}x")

# Scale glyphs by 3x vertically (1.5x for Tall * 2 = 3x)
scale_factor = 3.0

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

    # Skip empty glyphs
    if not glyph.isComposite() and glyph.numberOfContours == 0:
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
    glyf_table[glyph_name] = tt_pen.glyph()

# Update font metrics in OS/2 table
os2.sTypoAscender = new_ascent
os2.sTypoDescender = new_descent
os2.usWinAscent = new_ascent
os2.usWinDescent = abs(new_descent)

# Update hhea table
hhea.ascent = new_ascent
hhea.descent = new_descent

# Update bounding box in head table if needed
head.yMin = new_descent
head.yMax = new_ascent

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
