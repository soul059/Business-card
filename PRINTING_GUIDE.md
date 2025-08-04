# Business Card Printing Guide

## Files Created

1. **business_cards_multiple_A4.html** - 10 business cards per A4 page (economical printing)
2. **business_cards_single_A4.html** - 1 business card centered on A4 page (template/preview)
3. **print_business_cards.py** - Python script to open files in browser
4. **open_for_printing.bat** - Windows batch script to open files

## Quick Start

### Option 1: Use the Python Script
```bash
python print_business_cards.py
```

### Option 2: Use the Batch File (Windows)
Double-click `open_for_printing.bat`

### Option 3: Manual Method
1. Double-click the HTML files to open them in your browser
2. Press Ctrl+P to print

## Printing Instructions

### Browser Print Settings
1. **Press Ctrl+P** in the browser
2. **Destination:** Choose "Save as PDF" or select your printer
3. **Paper size:** A4
4. **Margins:** Minimum or Custom (10mm)
5. **More settings:**
   - ✅ Enable "Background graphics"
   - ✅ Enable "Headers and footers" (optional)

### Physical Printing
- **Paper:** 250-300gsm cardstock (recommended)
- **Quality:** Highest/Photo quality settings
- **Orientation:** Portrait
- **Scaling:** 100% (do not scale)

## Card Specifications

- **Size:** 85mm × 55mm (standard business card size)
- **Format:** Front and back designs are side by side
- **Cutting:** Cut along dashed lines, then cut vertically in middle to separate front/back

## File Descriptions

### Multiple Cards Layout
- **File:** `business_cards_multiple_A4.html`
- **Layout:** 2 columns × 5 rows = 10 cards per page
- **Use case:** Economical printing for multiple copies
- **Best for:** Production printing

### Single Card Layout  
- **File:** `business_cards_single_A4.html`
- **Layout:** 1 card centered on page
- **Use case:** Template preview, single card printing
- **Best for:** Testing print quality, single copies

## Troubleshooting

### If colors don't print
- Enable "Background graphics" in browser print settings
- Try a different browser (Chrome, Firefox, Edge)

### If size is wrong
- Ensure scaling is set to 100%
- Check paper size is set to A4
- Verify printer settings match browser settings

### Alternative Methods

1. **Online Converters:**
   - Upload the SVG file to CloudConvert.com
   - Use Convertio.co for SVG to PDF conversion

2. **Design Software:**
   - Open SVG in Adobe Illustrator
   - Import into Inkscape (free)
   - Use Canva or similar online tools

3. **Direct Browser Method:**
   - Open `business_card_print_ready.svg` directly in browser
   - Adjust print settings manually
   - Print or save as PDF

## Support

If you encounter issues:
1. Try different browsers (Chrome works best)
2. Update your browser to the latest version
3. Check that JavaScript is enabled
4. Ensure popup blockers aren't interfering

## Final Tips

- **Test print:** Do a test print on regular paper first
- **Color calibration:** Check colors on screen vs printed output
- **Cutting guides:** Use the dashed lines as cutting guides
- **Professional printing:** For best results, use a professional printer service
- **File sharing:** The HTML files are self-contained and can be shared easily
