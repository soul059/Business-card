#!/usr/bin/env python3
"""
SVG to PDF Converter for Business Cards
Converts business_card_print_ready.svg to PDF with proper A4 layout using svglib
"""

import os
import sys
from pathlib import Path

try:
    from svglib.svglib import renderSVG
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.graphics import renderPDF
    from reportlab.graphics.shapes import Drawing, Group
    import tempfile
    import xml.etree.ElementTree as ET
except ImportError as e:
    print(f"Missing required library: {e}")
    print("Please install required packages:")
    print("pip install svglib reportlab")
    sys.exit(1)

def create_business_card_pdf(svg_file_path, output_pdf_path):
    """
    Convert SVG business card to PDF with multiple cards per A4 page
    """
    # A4 dimensions in points
    page_width, page_height = A4
    
    # Business card dimensions (85mm x 55mm - standard size)
    card_width_mm = 85
    card_height_mm = 55
    card_width = card_width_mm * mm
    card_height = card_height_mm * mm
    
    print(f"Converting {svg_file_path} to PDF...")
    print(f"A4 page size: {page_width/mm:.1f}mm x {page_height/mm:.1f}mm")
    print(f"Card size: {card_width_mm}mm x {card_height_mm}mm")
    
    try:
        # Load SVG and convert to ReportLab drawing
        drawing = renderSVG.renderSVG(svg_file_path)
        
        # Create PDF
        c = canvas.Canvas(output_pdf_path, pagesize=A4)
        
        # Calculate layout
        margin = 10 * mm
        usable_width = page_width - 2 * margin
        usable_height = page_height - 2 * margin
        
        # Calculate how many cards fit
        cards_horizontal = int(usable_width // card_width)
        cards_vertical = int(usable_height // card_height)
        cards_per_page = cards_horizontal * cards_vertical
        
        print(f"Cards per page: {cards_horizontal} x {cards_vertical} = {cards_per_page}")
        
        # Calculate spacing
        h_spacing = usable_width / cards_horizontal if cards_horizontal > 0 else usable_width
        v_spacing = usable_height / cards_vertical if cards_vertical > 0 else usable_height
        
        # Add title
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, page_height - margin/2, f"Business Cards - Print Template")
        
        # Scale factor for the drawing
        if drawing.width > 0 and drawing.height > 0:
            scale_x = card_width / drawing.width
            scale_y = card_height / drawing.height
            scale = min(scale_x, scale_y)
        else:
            scale = 1
        
        # Place cards on the page
        for row in range(cards_vertical):
            for col in range(cards_horizontal):
                x = margin + col * h_spacing + (h_spacing - card_width) / 2
                y = page_height - margin - (row + 1) * v_spacing + (v_spacing - card_height) / 2
                
                # Save state and apply transformations
                c.saveState()
                c.translate(x, y)
                c.scale(scale, scale)
                
                # Render the SVG drawing
                renderPDF.draw(drawing, c, 0, 0)
                
                c.restoreState()
                
                # Add cut lines
                c.setStrokeColorRGB(0.8, 0.8, 0.8)
                c.setLineWidth(0.5)
                c.setDash([2, 2])
                c.rect(x, y, card_width, card_height)
                c.setDash([])
        
        # Add printing instructions
        c.setFont("Helvetica", 8)
        instructions = [
            "Printing Instructions:",
            "1. Print on 250-300gsm cardstock for best results",
            "2. Use high-quality/photo printing settings", 
            "3. Cut along the dotted lines",
            "4. Each card measures 85mm x 55mm (standard business card size)",
            "5. The design shows both front and back - cut in the middle to separate"
        ]
        
        y_pos = margin - 15*mm
        for instruction in instructions:
            c.drawString(margin, y_pos, instruction)
            y_pos -= 3*mm
        
        c.save()
        print(f"PDF saved successfully: {output_pdf_path}")
        return True
        
    except Exception as e:
        print(f"Error converting SVG to PDF: {e}")
        return False

def create_single_card_pdf(svg_file_path, output_pdf_path):
    """
    Create a PDF with a single business card centered on A4 page
    """
    page_width, page_height = A4
    
    print(f"Creating single card PDF: {output_pdf_path}")
    
    try:
        # Load SVG
        drawing = renderSVG.renderSVG(svg_file_path)
        
        # Create PDF
        c = canvas.Canvas(output_pdf_path, pagesize=A4)
        
        # Business card dimensions
        card_width = 85 * mm
        card_height = 55 * mm
        
        # Center the card on the page
        x = (page_width - card_width) / 2
        y = (page_height - card_height) / 2
        
        # Add title
        c.setFont("Helvetica-Bold", 14)
        title_text = "Business Card - Print Template"
        title_width = c.stringWidth(title_text, "Helvetica-Bold", 14)
        c.drawString((page_width - title_width) / 2, y + card_height + 20*mm, title_text)
        
        # Calculate scale
        if drawing.width > 0 and drawing.height > 0:
            scale_x = card_width / drawing.width
            scale_y = card_height / drawing.height
            scale = min(scale_x, scale_y)
        else:
            scale = 1
        
        # Draw the card
        c.saveState()
        c.translate(x, y)
        c.scale(scale, scale)
        renderPDF.draw(drawing, c, 0, 0)
        c.restoreState()
        
        # Add cut lines
        c.setStrokeColorRGB(0.5, 0.5, 0.5)
        c.setLineWidth(1)
        c.setDash([3, 3])
        c.rect(x, y, card_width, card_height)
        c.setDash([])
        
        # Add measurements
        c.setFont("Helvetica", 8)
        c.setStrokeColorRGB(0.3, 0.3, 0.3)
        
        # Horizontal measurement
        c.line(x, y - 5*mm, x + card_width, y - 5*mm)
        c.line(x, y - 3*mm, x, y - 7*mm)
        c.line(x + card_width, y - 3*mm, x + card_width, y - 7*mm)
        c.drawCentredText(x + card_width/2, y - 8*mm, "85mm")
        
        # Vertical measurement
        c.line(x - 5*mm, y, x - 5*mm, y + card_height)
        c.line(x - 3*mm, y, x - 7*mm, y)
        c.line(x - 3*mm, y + card_height, x - 7*mm, y + card_height)
        
        # Rotate text for vertical measurement
        c.saveState()
        c.translate(x - 10*mm, y + card_height/2)
        c.rotate(90)
        c.drawCentredText(0, 0, "55mm")
        c.restoreState()
        
        # Add instructions
        instructions = [
            "Printing Instructions:",
            "• Print on high-quality cardstock (250-300gsm recommended)",
            "• Use highest quality print settings",
            "• Cut carefully along the dashed lines",
            "• Standard business card size: 85mm × 55mm",
            "",
            "The card contains both front and back designs side by side.",
            "Cut vertically in the middle to separate front and back."
        ]
        
        y_pos = y - 20*mm
        for instruction in instructions:
            if instruction.startswith("•"):
                c.drawString(x + 10*mm, y_pos, instruction)
            else:
                c.drawString(x, y_pos, instruction)
            y_pos -= 4*mm
        
        c.save()
        print(f"Single card PDF saved: {output_pdf_path}")
        return True
        
    except Exception as e:
        print(f"Error creating single card PDF: {e}")
        return False

def create_simple_pdf_fallback(svg_file_path, output_pdf_path):
    """
    Fallback method: Create a simple PDF with SVG converted to text instructions
    """
    print("Creating fallback PDF with printing instructions...")
    
    page_width, page_height = A4
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, page_height - 50, "Business Card Print Instructions")
    
    # Main instructions
    c.setFont("Helvetica", 12)
    y_pos = page_height - 100
    
    instructions = [
        "Your business card SVG file is ready for printing!",
        "",
        "Method 1: Print directly from web browser",
        "1. Open the SVG file in a web browser (Chrome, Firefox, Edge)",
        "2. Press Ctrl+P to print",
        "3. Set paper size to A4",
        "4. Adjust scale to fit the page",
        "5. Select high-quality printing",
        "",
        "Method 2: Use online SVG to PDF converters",
        "• CloudConvert.com",
        "• Convertio.co", 
        "• Adobe Acrobat online tools",
        "",
        "Method 3: Use design software",
        "• Adobe Illustrator",
        "• Inkscape (free)",
        "• GIMP with SVG support",
        "",
        "Printing Tips:",
        "• Use 250-300gsm cardstock paper",
        "• Print at highest quality settings",
        "• The SVG shows both front and back side by side",
        "• Each card should measure 85mm × 55mm when printed",
        "• Cut carefully to separate front and back",
        "",
        f"SVG file location: {svg_file_path}",
    ]
    
    for instruction in instructions:
        if instruction.startswith("•"):
            c.drawString(70, y_pos, instruction)
        elif instruction.startswith("Method") or instruction.startswith("Printing"):
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y_pos, instruction)
            c.setFont("Helvetica", 12)
        else:
            c.drawString(50, y_pos, instruction)
        y_pos -= 15
        
        if y_pos < 50:  # Start new page if needed
            c.showPage()
            y_pos = page_height - 50
    
    c.save()
    print(f"Fallback PDF created: {output_pdf_path}")

def main():
    # File paths
    script_dir = Path(__file__).parent
    svg_file = script_dir / "business_card_print_ready.svg"
    
    if not svg_file.exists():
        print(f"Error: SVG file not found: {svg_file}")
        return
    
    print("Creating business card PDFs...\n")
    
    # Try to create the advanced PDFs
    success = False
    
    # Multiple cards per page
    multiple_pdf = script_dir / "business_cards_multiple_A4.pdf"
    if create_business_card_pdf(str(svg_file), str(multiple_pdf)):
        success = True
        print()
    
    # Single card centered
    single_pdf = script_dir / "business_card_single_A4.pdf" 
    if create_single_card_pdf(str(svg_file), str(single_pdf)):
        success = True
        print()
    
    # Create fallback instructions PDF
    fallback_pdf = script_dir / "business_card_printing_instructions.pdf"
    create_simple_pdf_fallback(str(svg_file), str(fallback_pdf))
    
    print(f"\nConversion complete!")
    
    if success:
        print(f"Files created:")
        if multiple_pdf.exists():
            print(f"  1. {multiple_pdf.name} - Multiple cards per A4 page")
        if single_pdf.exists(): 
            print(f"  2. {single_pdf.name} - Single card centered on A4")
        print(f"  3. {fallback_pdf.name} - Printing instructions and alternatives")
    else:
        print(f"Note: Advanced PDF conversion had issues.")
        print(f"Created: {fallback_pdf.name} with detailed printing instructions")
    
    print(f"\nReady for printing!")

if __name__ == "__main__":
    main()
