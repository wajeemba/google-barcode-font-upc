# Google Barcode Font - Libre Barcode 128 Modified

This repository contains modified versions of the Libre Barcode 128 font optimized for better barcode display.

## Overview

The original Libre Barcode 128 font has been modified into two taller variants, making barcodes more readable and properly proportioned. This is particularly useful when barcodes need to be displayed with better vertical spacing and visibility, especially in applications like Excel where vertical stretching isn't available.

## Font Variants

### Tall Version (`LibreBarcode128-Tall.ttf`)
- **Vertical scaling**: Glyphs scaled to 150% of original height
- **Descender expansion**: Uses full original height (1000 units) below baseline
- **Ascender expansion**: Adds 50% of original height (500 units) above baseline
- **Total height increase**: From 1,000 to 2,100 units (210% of original)

### Very Tall Version (`LibreBarcode128-VeryTall.ttf`)
- **Vertical scaling**: Glyphs scaled to 346% of original height (1.65x of Tall)
- **Proportions**: Uses same ascender/descender ratio as Tall version
- **Ascender**: 1,815 units (52.4% of total height)
- **Descender**: -1,650 units (47.6% of total height)
- **Total height increase**: From 1,000 to 3,465 units (346% of original)
- **Use case**: Perfect for very long UPCs in Excel where uniform height is needed

### Metrics Comparison

| Metric | Original | Tall | Very Tall |
|--------|----------|------|-----------|
| Ascent | 600 | 1,100 | 1,815 |
| Descent | -400 | -1,000 | -1,650 |
| Total Height | 1,000 | 2,100 | 3,465 |
| Height vs Original | 1x | 2.1x | 3.46x |
| Height vs Tall | - | - | 1.65x |

## Files

- `fonts/LibreBarcode128-Regular.ttf` - Original font from Google Fonts
- `fonts/LibreBarcode128-Tall.ttf` - Tall variant (2.1x height)
- `fonts/LibreBarcode128-VeryTall.ttf` - Very Tall variant (3.46x height, 1.65x of Tall)
- `modify_font.py` - Python script to create the Tall variant
- `modify_font_verytall.py` - Python script to create the Very Tall variant
- `examine_font.py` - Utility script to examine font metrics

## Usage

Install one or both modified fonts on your system:

- **Tall variant** (`LibreBarcode128-Tall.ttf`): Good for most applications needing better vertical proportions
- **Very Tall variant** (`LibreBarcode128-VeryTall.ttf`): Perfect for Excel or other applications where very long barcodes need consistent height

Both fonts support Code 128 barcode encoding (no text variant).

## License

This project uses the Libre Barcode font family, which is licensed under the SIL Open Font License, Version 1.1.

See [LICENSE.md](LICENSE.md) for the full license text.

## Credits

- Original font: [Libre Barcode Project](https://github.com/graphicore/librebarcode)
- Available on [Google Fonts](https://fonts.google.com/specimen/Libre+Barcode+128)

## Building

To regenerate the modified fonts, ensure you have Python 3 and fonttools installed:

```bash
pip install fonttools

# Generate Tall variant
python3 modify_font.py

# Generate Very Tall variant
python3 modify_font_verytall.py
```

The scripts will create:
- `fonts/LibreBarcode128-Tall.ttf` - From `modify_font.py`
- `fonts/LibreBarcode128-VeryTall.ttf` - From `modify_font_verytall.py`
