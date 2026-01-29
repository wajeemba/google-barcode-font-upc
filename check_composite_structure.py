#!/usr/bin/env python3
"""Check composite glyph structure in Tall font."""

from fontTools.ttLib import TTFont

tall = TTFont('fonts/LibreBarcode128-Tall.ttf')
glyf = tall['glyf']

# Check a composite glyph
glyph_name = 'uni0021.code.exclam'
if glyph_name in glyf:
    glyph = glyf[glyph_name]
    print(f"{glyph_name}:")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")

    if glyph.isComposite():
        print(f"  Components:")
        for component in glyph.components:
            print(f"    - {component.glyphName}")
            print(f"      Transform: {component.transform if hasattr(component, 'transform') else 'none'}")

            # Check the referenced glyph
            if component.glyphName in glyf:
                ref_glyph = glyf[component.glyphName]
                print(f"      Referenced glyph bounds: yMin={ref_glyph.yMin}, yMax={ref_glyph.yMax}")

# Also check the stoppattern which should be the tallest
if 'uni00CE.code.stoppattern' in glyf:
    glyph = glyf['uni00CE.code.stoppattern']
    print(f"\nuni00CE.code.stoppattern:")
    print(f"  Is composite: {glyph.isComposite()}")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
    if glyph.isComposite():
        print(f"  Components: {len(glyph.components)}")

tall.close()
