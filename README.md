# Google Barcode Font - Libre Barcode 128 Modified

This repository contains a modified version of the Libre Barcode 128 font optimized for better barcode display.

## Overview

The original Libre Barcode 128 font has been modified to be taller, making barcodes more readable and properly proportioned. This is particularly useful when barcodes need to be displayed with better vertical spacing and visibility.

## Modifications

The modified font (`LibreBarcode128-Tall.ttf`) has the following changes:

- **Vertical scaling**: Glyphs are scaled to 150% of their original height
- **Descender expansion**: Uses the full original height (1000 units) below the baseline for better spacing
- **Ascender expansion**: Adds 50% of the original height (500 units) above the current ascent
- **Total height increase**: From 1000 units to 2,100 units (210% of original)

### Metrics Comparison

| Metric | Original | Modified |
|--------|----------|----------|
| Ascent | 600 | 1,100 |
| Descent | -400 | -1,000 |
| Total Height | 1,000 | 2,100 |

## Files

- `fonts/LibreBarcode128-Regular.ttf` - Original font from Google Fonts
- `fonts/LibreBarcode128-Tall.ttf` - Modified font optimized for better display
- `modify_font.py` - Python script used to create the modified font
- `examine_font.py` - Utility script to examine font metrics

## Usage

Install the modified font (`LibreBarcode128-Tall.ttf`) on your system and use it in your applications where you need to display Code 128 barcodes with better vertical proportions.

The font supports Code 128 barcode encoding (no text variant).

## License

This project uses the Libre Barcode font family, which is licensed under the SIL Open Font License, Version 1.1.

See [LICENSE.md](LICENSE.md) for the full license text.

## Credits

- Original font: [Libre Barcode Project](https://github.com/graphicore/librebarcode)
- Available on [Google Fonts](https://fonts.google.com/specimen/Libre+Barcode+128)

## Building

To regenerate the modified font, ensure you have Python 3 and fonttools installed:

```bash
pip install fonttools
python3 modify_font.py
```

The script will create `fonts/LibreBarcode128-Tall.ttf` from the original font file.
