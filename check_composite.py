#!/usr/bin/env python3
"""Check if uni glyphs are composite."""

from fontTools.ttLib import TTFont

print("=== ORIGINAL FONT ===")
font = TTFont('fonts/LibreBarcode128-Regular.ttf')
glyf = font['glyf']

# Check a sample uni glyph
if 'uni0041.code.A' in glyf:
    glyph = glyf['uni0041.code.A']
    print(f"uni0041.code.A:")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  Number of contours: {glyph.numberOfContours}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
    if glyph.isComposite():
        print(f"  Components: {glyph.components}")

if 'code.A' in glyf:
    glyph = glyf['code.A']
    print(f"\ncode.A:")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  Number of contours: {glyph.numberOfContours}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")

font.close()

print("\n=== VERYTALL FONT ===")
font = TTFont('fonts/LibreBarcode128-VeryTall.ttf')
glyf = font['glyf']

if 'uni0041.code.A' in glyf:
    glyph = glyf['uni0041.code.A']
    print(f"uni0041.code.A:")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  Number of contours: {glyph.numberOfContours}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
    if glyph.isComposite():
        print(f"  Components: {glyph.components}")

if 'code.A' in glyf:
    glyph = glyf['code.A']
    print(f"\ncode.A:")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  Number of contours: {glyph.numberOfContours}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")

font.close()
