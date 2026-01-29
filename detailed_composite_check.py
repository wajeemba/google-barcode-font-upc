#!/usr/bin/env python3
"""Detailed check of composite glyphs."""

from fontTools.ttLib import TTFont

print("=== ORIGINAL FONT ===")
original = TTFont('fonts/LibreBarcode128-Regular.ttf')
orig_glyf = original['glyf']

if 'uni0041.code.A' in orig_glyf:
    glyph = orig_glyf['uni0041.code.A']
    print(f"uni0041.code.A:")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
    if glyph.isComposite():
        for i, component in enumerate(glyph.components):
            print(f"  Component {i}:")
            print(f"    glyphName: {component.glyphName}")
            print(f"    x: {component.x}, y: {component.y}")
            # Check if there's a scale
            if hasattr(component, 'transform'):
                print(f"    transform: {component.transform}")
            # Check flags
            print(f"    flags: {component.flags}")

if 'code.A' in orig_glyf:
    glyph = orig_glyf['code.A']
    print(f"\ncode.A:")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")

print("\n=== TALL FONT ===")
tall = TTFont('fonts/LibreBarcode128-Tall.ttf')
tall_glyf = tall['glyf']

if 'uni0041.code.A' in tall_glyf:
    glyph = tall_glyf['uni0041.code.A']
    print(f"uni0041.code.A:")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")
    if glyph.isComposite():
        for i, component in enumerate(glyph.components):
            print(f"  Component {i}:")
            print(f"    glyphName: {component.glyphName}")
            print(f"    x: {component.x}, y: {component.y}")
            if hasattr(component, 'transform'):
                print(f"    transform: {component.transform}")
            print(f"    flags: {component.flags}")

if 'code.A' in tall_glyf:
    glyph = tall_glyf['code.A']
    print(f"\ncode.A:")
    print(f"  yMin: {glyph.yMin}, yMax: {glyph.yMax}")

original.close()
tall.close()
