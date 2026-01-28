#!/usr/bin/env python3
"""Detailed debugging of all three fonts."""

from fontTools.ttLib import TTFont

fonts = {
    'Original': 'fonts/LibreBarcode128-Regular.ttf',
    'Tall': 'fonts/LibreBarcode128-Tall.ttf',
    'VeryTall': 'fonts/LibreBarcode128-VeryTall.ttf'
}

for font_name, font_path in fonts.items():
    print(f"\n{'='*60}")
    print(f"{font_name}: {font_path}")
    print('='*60)

    font = TTFont(font_path)
    os2 = font['OS/2']
    head = font['head']
    glyf = font['glyf']

    print(f"\nMetrics:")
    print(f"  sTypoAscender: {os2.sTypoAscender}")
    print(f"  sTypoDescender: {os2.sTypoDescender}")
    print(f"  Line Height: {os2.sTypoAscender - os2.sTypoDescender}")
    print(f"  usWinAscent: {os2.usWinAscent}")
    print(f"  usWinDescent: {os2.usWinDescent}")
    print(f"  Win Height: {os2.usWinAscent + os2.usWinDescent}")

    print(f"\nHead table bounding box:")
    print(f"  xMin: {head.xMin}, xMax: {head.xMax}")
    print(f"  yMin: {head.yMin}, yMax: {head.yMax}")

    # Find actual glyph bounds
    actual_min_y = float('inf')
    actual_max_y = float('-inf')
    sample_glyphs = []

    for glyph_name in font.getGlyphOrder():
        if glyph_name in glyf and glyph_name != '.notdef':
            glyph = glyf[glyph_name]
            if hasattr(glyph, 'yMin') and hasattr(glyph, 'yMax'):
                if glyph.numberOfContours > 0:
                    actual_min_y = min(actual_min_y, glyph.yMin)
                    actual_max_y = max(actual_max_y, glyph.yMax)
                    if len(sample_glyphs) < 3:
                        sample_glyphs.append((glyph_name, glyph.yMin, glyph.yMax))

    print(f"\nActual glyph bounds:")
    print(f"  Actual yMin: {actual_min_y}")
    print(f"  Actual yMax: {actual_max_y}")
    print(f"  Actual glyph height: {actual_max_y - actual_min_y}")

    print(f"\nSample glyphs:")
    for name, ymin, ymax in sample_glyphs:
        print(f"  {name}: yMin={ymin}, yMax={ymax}, height={ymax-ymin}")

    # Check for potential clipping issues
    print(f"\nPotential issues:")
    if actual_max_y > os2.usWinAscent:
        print(f"  WARNING: Glyphs extend above usWinAscent! ({actual_max_y} > {os2.usWinAscent})")
    if actual_min_y < -os2.usWinDescent:
        print(f"  WARNING: Glyphs extend below usWinDescent! ({actual_min_y} < {-os2.usWinDescent})")
    if head.yMax != actual_max_y:
        print(f"  WARNING: head.yMax ({head.yMax}) doesn't match actual ({actual_max_y})")
    if head.yMin != actual_min_y:
        print(f"  WARNING: head.yMin ({head.yMin}) doesn't match actual ({actual_min_y})")

    font.close()
