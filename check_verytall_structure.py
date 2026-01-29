#!/usr/bin/env python3
"""Check Very Tall font structure."""

from fontTools.ttLib import TTFont

verytall = TTFont('fonts/LibreBarcode128-VeryTall.ttf')
glyf = verytall['glyf']

# Check a base glyph
if 'code.A' in glyf:
    glyph = glyf['code.A']
    print("code.A (base glyph):")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
    print(f"  Height: {glyph.yMax - glyph.yMin}")

# Check a composite glyph
glyph_name = 'uni0041.code.A'
if glyph_name in glyf:
    glyph = glyf[glyph_name]
    print(f"\n{glyph_name} (composite glyph):")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
    print(f"  Height: {glyph.yMax - glyph.yMin}")

    if glyph.isComposite():
        print(f"  Components:")
        for component in glyph.components:
            print(f"    - {component.glyphName}")
            print(f"      Transform: {component.transform if hasattr(component, 'transform') else 'none'}")

# Check the original font to see the original transform
print("\n=== ORIGINAL FONT ===")
original = TTFont('fonts/LibreBarcode128-Regular.ttf')
orig_glyf = original['glyf']

if 'uni0041.code.A' in orig_glyf:
    glyph = orig_glyf['uni0041.code.A']
    print(f"\nOriginal uni0041.code.A:")
    print(f"  Is composite: {glyph.isComposite()}")
    if glyph.isComposite():
        print(f"  Components:")
        for component in glyph.components:
            print(f"    - {component.glyphName}")
            print(f"      Transform: {component.transform if hasattr(component, 'transform') else 'none'}")

original.close()
verytall.close()
