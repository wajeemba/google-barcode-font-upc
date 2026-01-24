# Google Barcode Font - UPC Encoding (Modified)

This repository contains a modified version of the Libre Barcode EAN13 font, optimized for UPC encoding with enhanced vertical dimensions.

## Font Modifications

The font has been modified to be **150% taller** than the original:

- **Original height**: 960 units (Ascender: 840, Descender: 120)
- **Modified height**: 1440 units (Ascender: 1320, Descender: 120)
- **Height multiplier**: 1.5x

### Vertical Metrics Distribution

- **Descender**: Kept at 100% of original (120 units below baseline)
- **Ascender**: Increased by 50% of original total height (1320 units above baseline)

This ensures the barcode displays properly with adequate height while maintaining the full descender depth.

## Files

- `fonts/LibreBarcodeEAN13Text-Regular.ttf` - Original Libre Barcode EAN13 Text font
- `fonts/LibreBarcodeEAN13Text-Tall-Regular.ttf` - Modified 150% taller version
- `modify_font.py` - Python script used to modify the font metrics
- `LICENSE.md` - SIL Open Font License

## Usage

Use the `LibreBarcodeEAN13Text-Tall-Regular.ttf` font for UPC/EAN13 barcode encoding. The font supports:

- UPC-A
- UPC-E
- EAN-13
- EAN-8

## License

This font is licensed under the SIL Open Font License 1.1. See [LICENSE.md](LICENSE.md) for details.

## Attribution

Based on [Libre Barcode](https://github.com/graphicore/librebarcode) by The Libre Barcode Project Authors.

## Note on Text Variant

The Libre Barcode EAN13 font is only available in a "Text" variant, which includes human-readable numbers below the barcode. There is no separate "no-text" variant for EAN13 in the Libre Barcode project, unlike Code 39 and Code 128 which have both variants.
