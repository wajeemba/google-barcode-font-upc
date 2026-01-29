#!/usr/bin/env python3
"""Check specific base glyphs in all fonts."""

from fontTools.ttLib import TTFont

fonts = [
    ('Original', 'fonts/LibreBarcode128-Regular.ttf'),
    ('Tall', 'fonts/LibreBarcode128-Tall.ttf'),
    ('Very Tall', 'fonts/LibreBarcode128-VeryTall.ttf')
]

for name, path in fonts:
    font = TTFont(path)
    glyf = font['glyf']

    print(f"\n{name}:")

    # Check base glyph
    if 'code.A' in glyf:
        glyph = glyf['code.A']
        print(f"  code.A: yMax={glyph.yMax}, composite={glyph.isComposite()}")

    # Check composite glyph
    if 'uni0041.code.A' in glyf:
        glyph = glyf['uni0041.code.A']
        print(f"  uni0041.code.A: yMax={glyph.yMax}, composite={glyph.isComposite()}")

    font.close()

print("\n\nExpected heights:")
print("  Original base: 590")
print("  Tall base: 590 * 1.5 = 885")
print("  Tall composite: 885 * 1.5 = 1327.5")
print("  Very Tall base: 885 * 1.65 = 1460.25")
print("  Very Tall composite: 1460.25 * 1.5 = 2190.375")
