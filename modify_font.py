#!/usr/bin/env python3
"""
Modify the Libre Barcode EAN13 font to be 150% taller.
Keeps the descender at 100% (same as current) and adds 50% to the ascender.
"""

from fontTools import ttLib
import sys

# File paths
input_font = 'fonts/LibreBarcodeEAN13Text-Regular.ttf'
output_font = 'fonts/LibreBarcodeEAN13Text-Tall-Regular.ttf'

print("Loading font...")
font = ttLib.TTFont(input_font)

# Get current metrics
os2 = font['OS/2']
hhea = font['hhea']

current_ascender = os2.sTypoAscender
current_descender = abs(os2.sTypoDescender)
current_height = current_ascender + current_descender

print(f"\nCurrent metrics:")
print(f"  Ascender: {current_ascender}")
print(f"  Descender: {current_descender}")
print(f"  Total height: {current_height}")

# Calculate new metrics
# Descender stays the same (100% of current)
new_descender = current_descender

# Add 50% of total current height to ascender
height_increase = int(0.5 * current_height)
new_ascender = current_ascender + height_increase

new_height = new_ascender + new_descender

print(f"\nNew metrics:")
print(f"  Ascender: {new_ascender} (+{height_increase})")
print(f"  Descender: {new_descender} (unchanged)")
print(f"  Total height: {new_height}")
print(f"  Height multiplier: {new_height / current_height:.2f}x")

# Update OS/2 table
os2.sTypoAscender = new_ascender
os2.sTypoDescender = -new_descender  # Negative value
os2.usWinAscent = new_ascender
os2.usWinDescent = new_descender  # Positive value

# Update hhea table
hhea.ascent = new_ascender
hhea.descent = -new_descender  # Negative value

# Update font metadata to reflect modification
if 'name' in font:
    name_table = font['name']
    # Update the full font name
    for record in name_table.names:
        if record.nameID == 4:  # Full font name
            if hasattr(record.string, 'decode'):
                current_name = record.string.decode('utf-16-be' if record.platformID == 3 else 'latin-1')
            else:
                current_name = str(record.string)
            new_name = current_name.replace('Regular', 'Tall Regular')
            if 'Tall' not in new_name:
                new_name = current_name + ' Tall'

            if record.platformID == 3:  # Windows
                record.string = new_name.encode('utf-16-be')
            else:
                record.string = new_name.encode('latin-1')

print(f"\nSaving modified font to {output_font}...")
font.save(output_font)
font.close()

print("Done!")
