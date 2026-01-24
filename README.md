# Google Barcode Font for UPC

This repository contains a modified version of the Libre Barcode EAN13 font optimized for UPC barcode display.

## Overview

The original Libre Barcode EAN13 Text font has been modified to be taller, making UPC barcodes more readable and properly proportioned. This is particularly useful when barcodes need to be displayed with better vertical spacing and visibility.

## Modifications

The modified font (`LibreBarcodeEAN13Text-UPC.ttf`) has the following changes:

- **Vertical scaling**: Glyphs are scaled to 150% of their original height
- **Descender expansion**: Uses the full original height (960 units) below the baseline for better spacing
- **Ascender expansion**: Adds 50% of the original height (480 units) above the current ascent
- **Total height increase**: From 960 units to 2,280 units (237.5% of original)

### Metrics Comparison

| Metric | Original | Modified |
|--------|----------|----------|
| Ascent | 840 | 1,320 |
| Descent | -120 | -960 |
| Total Height | 960 | 2,280 |

## Files

- `fonts/LibreBarcodeEAN13Text-Regular.ttf` - Original font from Google Fonts
- `fonts/LibreBarcodeEAN13Text-UPC.ttf` - Modified font optimized for UPC display
- `modify_font.py` - Python script used to create the modified font
- `examine_font.py` - Utility script to examine font metrics

## Usage

Install the modified font (`LibreBarcodeEAN13Text-UPC.ttf`) on your system and use it in your applications where you need to display UPC barcodes with better vertical proportions.

The font supports:
- EAN-13
- EAN-8
- UPC-A
- UPC-E
- 2-digit and 5-digit add-ons

## License

This project uses the Libre Barcode font family, which is licensed under the SIL Open Font License, Version 1.1.

See [LICENSE.md](LICENSE.md) for the full license text.

## Credits

- Original font: [Libre Barcode Project](https://github.com/graphicore/librebarcode)
- Available on [Google Fonts](https://fonts.google.com/specimen/Libre+Barcode+EAN13+Text)

## Building

To regenerate the modified font, ensure you have Python 3 and fonttools installed:

```bash
pip install fonttools
python3 modify_font.py
```

The script will create `fonts/LibreBarcodeEAN13Text-UPC.ttf` from the original font file.
