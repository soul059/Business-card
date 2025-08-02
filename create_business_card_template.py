#!/usr/bin/env python3
"""
Business Card Template Generator for GIMP
Creates a print-ready business card template in multiple formats
Standard business card size: 85mm x 85mm (square format)
300 DPI for print quality
"""

import os

def create_gimp_script():
    """Generate a GIMP Script-Fu script to create the business card template"""
    
    script_content = '''
; GIMP Script-Fu for Business Card Template
; Square format: 85mm x 85mm at 300 DPI

(define (create-business-card-template)
  (let* (
    ; Convert mm to pixels at 300 DPI: 85mm = 1003 pixels
    (img-width 1003)
    (img-height 1003)
    (img (car (gimp-image-new img-width img-height RGB)))
    (front-layer (car (gimp-layer-new img img-width img-height RGB-IMAGE "Card Front" 100 NORMAL-MODE)))
    (back-layer (car (gimp-layer-new img img-width img-height RGB-IMAGE "Card Back" 100 NORMAL-MODE)))
    (margin 60) ; 5mm margin in pixels
    )
    
    ; Add layers to image
    (gimp-image-add-layer img front-layer 0)
    (gimp-image-add-layer img back-layer 1)
    
    ; Set resolution for print
    (gimp-image-set-resolution img 300 300)
    
    ; Create front card background
    (gimp-context-set-foreground '(26 26 46)) ; Dark blue background
    (gimp-drawable-fill front-layer FOREGROUND-FILL)
    
    ; Create back card background  
    (gimp-context-set-foreground '(26 26 46)) ; Dark blue background
    (gimp-drawable-fill back-layer FOREGROUND-FILL)
    
    ; Add text layers for front card
    (let* ((name-text (car (gimp-text-fontname img -1 100 100 "KEVAL CHAUHAN" 0 TRUE 36 PIXELS "Arial Bold"))))
      (gimp-text-layer-set-color name-text '(255 255 255))
      (gimp-image-add-layer img name-text 0))
    
    (let* ((title-text (car (gimp-text-fontname img -1 100 150 "Web Developer" 0 TRUE 20 PIXELS "Arial"))))
      (gimp-text-layer-set-color title-text '(233 69 96))
      (gimp-image-add-layer img title-text 0))
    
    ; Add contact information text
    (let* ((phone-text (car (gimp-text-fontname img -1 150 220 "📞 +91 9429806587" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color phone-text '(255 255 255))
      (gimp-image-add-layer img phone-text 0))
    
    (let* ((email-text (car (gimp-text-fontname img -1 150 250 "✉ keval.chauhan@email.com" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color email-text '(255 255 255))
      (gimp-image-add-layer img email-text 0))
    
    (let* ((website-text (car (gimp-text-fontname img -1 150 280 "🌐 keval.live" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color website-text '(255 255 255))
      (gimp-image-add-layer img website-text 0))
    
    (let* ((linkedin-text (car (gimp-text-fontname img -1 150 310 "💼 linkedin.com/in/keval-s-chauhan" 0 TRUE 14 PIXELS "Arial"))))
      (gimp-text-layer-set-color linkedin-text '(255 255 255))
      (gimp-image-add-layer img linkedin-text 0))
    
    (let* ((github-text (car (gimp-text-fontname img -1 150 340 "💻 github.com/soul059" 0 TRUE 14 PIXELS "Arial"))))
      (gimp-text-layer-set-color github-text '(255 255 255))
      (gimp-image-add-layer img github-text 0))
    
    ; Add skills text
    (let* ((skills-text (car (gimp-text-fontname img -1 150 400 "Skills: HTML • CSS • JavaScript • React • Node.js • MongoDB" 0 TRUE 12 PIXELS "Arial"))))
      (gimp-text-layer-set-color skills-text '(255 255 255))
      (gimp-image-add-layer img skills-text 0))
    
    ; Add text for back card
    (gimp-image-set-active-layer img back-layer)
    
    (let* ((back-name-text (car (gimp-text-fontname img -1 300 100 "KEVAL CHAUHAN" 0 TRUE 32 PIXELS "Arial Bold"))))
      (gimp-text-layer-set-color back-name-text '(255 255 255))
      (gimp-image-add-layer img back-name-text 0))
    
    (let* ((qr-label-text (car (gimp-text-fontname img -1 350 800 "Scan for Digital Card" 0 TRUE 18 PIXELS "Arial"))))
      (gimp-text-layer-set-color qr-label-text '(255 255 255))
      (gimp-image-add-layer img qr-label-text 0))
    
    (let* ((url-text (car (gimp-text-fontname img -1 420 830 "keval.live" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color url-text '(233 69 96))
      (gimp-image-add-layer img url-text 0))
    
    ; Display the image
    (gimp-display-new img)
    
    ; Return the image
    img
  )
)

; Register the script
(script-fu-register
  "create-business-card-template"
  "Business Card Template"
  "Creates a square business card template (85mm x 85mm) for Keval Chauhan"
  "Assistant"
  "GPL"
  "2025"
  ""
)

(script-fu-menu-register "create-business-card-template" "<Image>/Filters/Generic")
'''
    
    return script_content

def create_instructions():
    """Create detailed instructions for using the templates"""
    
    instructions = """
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
   - Windows: `C:\\Users\\[username]\\AppData\\Roaming\\GIMP\\2.10\\scripts\\`
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
"""
    
    return instructions

# Create the files
def main():
    # Create GIMP script
    script_content = create_gimp_script()
    with open('business_card_gimp_script.scm', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    # Create instructions
    instructions = create_instructions()
    with open('printing_instructions.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Business card templates created successfully!")
    print("\nFiles generated:")
    print("- business_card_front.svg (Front design)")
    print("- business_card_back.svg (Back with QR placeholder)")
    print("- business_card_gimp_script.scm (GIMP script)")
    print("- printing_instructions.md (Detailed instructions)")
    print("\n📝 Next steps:")
    print("1. Generate a real QR code for your website")
    print("2. Add your actual photo")
    print("3. Follow printing_instructions.md for print preparation")

if __name__ == "__main__":
    main()
