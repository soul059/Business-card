
# Business Card Template Instructions

## Files Created:
1. `business_card_front.svg` - Front side design
2. `business_card_back.svg` - Back side with QR code placeholder
3. `business_card_gimp_script.scm` - GIMP Script-Fu for template creation
4. `printing_instructions.md` - This file

## Card Specifications:
- **Size**: 85mm x 85mm (Square format)
- **Resolution**: 300 DPI for print quality
- **Color Mode**: RGB (convert to CMYK before final printing)
- **Bleed Area**: Add 3mm bleed if required by printer

## Using the SVG Files:

### For Quick Printing:
1. Open the SVG files in any vector graphics software (Inkscape, Illustrator, etc.)
2. Replace the QR code placeholder with an actual QR code pointing to your website
3. Replace the photo placeholder with your actual photo
4. Export as high-resolution PDF or PNG (300 DPI)

### Generating QR Code:
1. Go to a QR code generator (like qr-code-generator.com)
2. Enter your website URL: `https://keval.live` (or your actual domain)
3. Download as SVG or high-resolution PNG
4. Replace the QR code placeholder in the back design

## Using with GIMP:

### Installing the Script:
1. Copy `business_card_gimp_script.scm` to your GIMP scripts folder:
   - Windows: `C:\Users\[username]\AppData\Roaming\GIMP\2.10\scripts\`
   - macOS: `~/Library/Application Support/GIMP/2.10/scripts/`
   - Linux: `~/.gimp-2.10/scripts/`

2. Restart GIMP or refresh scripts: `Filters > Script-Fu > Refresh Scripts`

3. Run the script: `Filters > Generic > Business Card Template`

### Customizing in GIMP:
1. The script creates a 1003x1003 pixel image (85mm at 300 DPI)
2. Edit text layers to update information
3. Add your photo by creating a new layer and importing the image
4. Create or import a real QR code for the back
5. Add any additional design elements

## Print Preparation:

### Before Printing:
1. **Convert to CMYK**: Most printers require CMYK color mode
2. **Check Colors**: Ensure colors will print correctly (screen vs print differences)
3. **Add Bleed**: Extend background colors 3mm beyond card edges if required
4. **Final Size**: Ensure final dimensions are exactly 85mm x 85mm

### Recommended Paper:
- **Weight**: 300-350 GSM cardstock
- **Finish**: Matte or semi-gloss for professional look
- **Paper Type**: Coated paper for best color reproduction

### Print Settings:
- **Resolution**: 300 DPI minimum
- **Color Profile**: Use printer's recommended CMYK profile
- **Scaling**: Ensure "Actual Size" or 100% scaling

## Professional Printing Tips:
1. **Order Test Print**: Always order 1-5 cards first to check quality
2. **Multiple Designs**: Consider slight variations in layout
3. **Quantity**: Order in multiples of 25 or 50 for better pricing
4. **Cutting**: Ensure precise cutting for professional appearance

## File Formats for Printing:
- **Best**: PDF with embedded fonts and high-resolution images
- **Good**: AI (Adobe Illustrator) or EPS files
- **Acceptable**: High-resolution PNG (300 DPI) or TIFF

## Troubleshooting:
- **Blurry Text**: Ensure text is vector-based, not rasterized
- **Color Issues**: Check color profiles and convert RGB to CMYK
- **Size Problems**: Verify dimensions in mm/inches, not just pixels
- **QR Code**: Test QR code before printing to ensure it works

## Contact Information Updates:
Remember to update the following in your templates:
- Phone number: +91 9429806587
- Email: keval.chauhan@email.com
- Website: keval.live
- LinkedIn: linkedin.com/in/keval-s-chauhan
- GitHub: github.com/soul059
