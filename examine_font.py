#!/usr/bin/env python3
"""Examine the font metrics to understand current proportions."""

from fontTools.ttLib import TTFont

# Load the font
font = TTFont('fonts/LibreBarcodeEAN13Text-Regular.ttf')

# Get the head table (font header)
head = font['head']
print(f"Units per EM: {head.unitsPerEm}")

# Get the OS/2 table (contains metrics)
os2 = font['OS/2']
print(f"\nOS/2 Metrics:")
print(f"  Ascent: {os2.sTypoAscender}")
print(f"  Descent: {os2.sTypoDescender}")
print(f"  Line Gap: {os2.sTypoLineGap}")
print(f"  Win Ascent: {os2.usWinAscent}")
print(f"  Win Descent: {os2.usWinDescent}")

# Get the hhea table (horizontal header)
hhea = font['hhea']
print(f"\nhhea Metrics:")
print(f"  Ascent: {hhea.ascent}")
print(f"  Descent: {hhea.descent}")
print(f"  Line Gap: {hhea.lineGap}")

# Get bbox from head table
print(f"\nBounding Box:")
print(f"  xMin: {head.xMin}")
print(f"  yMin: {head.yMin}")
print(f"  xMax: {head.xMax}")
print(f"  yMax: {head.yMax}")

font.close()
