#!/usr/bin/env python3
"""
Modify the LibreBarcode 128 font for better display.

The goal is to make the font 150% taller with the following proportions:
- Use descender for 100% (full current height below the baseline)
- Add remaining 50% above the current height
"""

from fontTools.ttLib import TTFont
from fontTools.pens.t2CharStringPen import T2CharStringPen
import os

# Load the font
input_font = 'fonts/LibreBarcode128-Regular.ttf'
output_font = 'fonts/LibreBarcode128-Tall.ttf'

print(f"Loading font: {input_font}")
font = TTFont(input_font)

# Get current metrics
head = font['head']
os2 = font['OS/2']
hhea = font['hhea']

current_ascent = os2.sTypoAscender  # 840
current_descent = os2.sTypoDescender  # -120
current_total = current_ascent + abs(current_descent)  # 960

print(f"\nCurrent metrics:")
print(f"  Ascent: {current_ascent}")
print(f"  Descent: {current_descent}")
print(f"  Total height: {current_total}")

# Calculate new metrics
# Descender: use 100% of current total height below baseline
new_descent = -current_total  # -960

# Ascent: add 50% of current total height to current ascent
height_addition = int(current_total * 0.5)  # 480
new_ascent = current_ascent + height_addition  # 1320

new_total = new_ascent + abs(new_descent)  # 2280

print(f"\nNew metrics:")
print(f"  Ascent: {new_ascent}")
print(f"  Descent: {new_descent}")
print(f"  Total height: {new_total}")
print(f"  Height increase: {new_total/current_total:.1%}")

# Now we need to scale the glyphs vertically to match the new metrics
# We'll scale them by 150% and adjust their positions

scale_factor = 1.5

# Get the glyph set
glyf_table = font['glyf']
hmtx_table = font['hmtx']

# For each glyph, we need to scale it vertically
print(f"\nScaling glyphs by {scale_factor}x vertically...")

from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

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
    # We want to scale vertically by 1.5x
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

# Update font name to indicate it's modified
name_table = font['name']
for record in name_table.names:
    if record.nameID == 1:  # Font Family name
        record.string = "Libre Barcode 128 Tall"
    elif record.nameID == 4:  # Full font name
        record.string = "Libre Barcode 128 Tall Regular"
    elif record.nameID == 6:  # PostScript name
        record.string = "LibreBarcode128-Tall"

print(f"\nSaving modified font: {output_font}")
font.save(output_font)
font.close()

print(f"✓ Font modification complete!")
print(f"  Original: {input_font}")
print(f"  Modified: {output_font}")
