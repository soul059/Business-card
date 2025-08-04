#!/usr/bin/env python3
"""
SVG to PDF Converter for Business Cards
Converts business_card_print_ready.svg to PDF with proper A4 layout
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
    from reportlab.graphics.shapes import Drawing
    import tempfile
except ImportError as e:
    print(f"Missing required library: {e}")
    print("Please install required packages:")
    print("pip install svglib reportlab")
    sys.exit(1)

def svg_to_pdf_a4(svg_file_path, output_pdf_path, cards_per_page=10):
    """
    Convert SVG business card to PDF with multiple cards per A4 page
    
    Args:
        svg_file_path (str): Path to the SVG file
        output_pdf_path (str): Path for the output PDF
        cards_per_page (int): Number of business cards to fit per page
    """
    
    # A4 dimensions in points (72 points = 1 inch)
    page_width, page_height = A4
    
    # Business card dimensions (standard: 85mm x 55mm)
    card_width_mm = 85
    card_height_mm = 55
    card_width = card_width_mm * mm
    card_height = card_height_mm * mm
    
    # Convert SVG to PNG first for better handling
    print(f"Converting {svg_file_path} to PDF...")
    
    # Read SVG content
    with open(svg_file_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    # Convert SVG to PNG using cairosvg
    png_data = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'))
    
    # Create PDF
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    
    # Calculate layout for multiple cards per page
    margin = 10 * mm
    usable_width = page_width - 2 * margin
    usable_height = page_height - 2 * margin
    
    # Calculate how many cards fit horizontally and vertically
    cards_horizontal = int(usable_width // card_width)
    cards_vertical = int(usable_height // card_height)
    cards_per_page_actual = cards_horizontal * cards_vertical
    
    print(f"A4 page size: {page_width/mm:.1f}mm x {page_height/mm:.1f}mm")
    print(f"Card size: {card_width_mm}mm x {card_height_mm}mm")
    print(f"Cards per page: {cards_horizontal} x {cards_vertical} = {cards_per_page_actual}")
    
    # Load the PNG image
    img = Image.open(io.BytesIO(png_data))
    
    # Calculate spacing
    h_spacing = usable_width / cards_horizontal
    v_spacing = usable_height / cards_vertical
    
    # Add title
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, page_height - margin + 5*mm, f"Business Cards - {cards_per_page_actual} per page")
    
    # Place cards on the page
    for row in range(cards_vertical):
        for col in range(cards_horizontal):
            x = margin + col * h_spacing + (h_spacing - card_width) / 2
            y = page_height - margin - (row + 1) * v_spacing + (v_spacing - card_height) / 2
            
            # Save PNG to temporary file for reportlab
            temp_png_path = "temp_card.png"
            with open(temp_png_path, 'wb') as temp_file:
                temp_file.write(png_data)
            
            # Draw the image
            c.drawImage(temp_png_path, x, y, width=card_width, height=card_height)
            
            # Add cut lines (optional)
            c.setStrokeColorRGB(0.8, 0.8, 0.8)
            c.setLineWidth(0.5)
            c.setDash([2, 2])
            c.rect(x, y, card_width, card_height)
            c.setDash([])  # Reset dash
    
    # Add instructions at the bottom
    c.setFont("Helvetica", 8)
    instructions = [
        "Printing Instructions:",
        "1. Print on 250-300gsm cardstock for best results",
        "2. Use high-quality/photo printing settings",
        "3. Cut along the dotted lines",
        "4. Each card measures 85mm x 55mm (standard business card size)"
    ]
    
    y_pos = margin - 5*mm
    for instruction in instructions:
        c.drawString(margin, y_pos, instruction)
        y_pos -= 3*mm
    
    # Clean up temp file
    if os.path.exists(temp_png_path):
        os.remove(temp_png_path)
    
    # Finalize PDF
    c.save()
    print(f"PDF saved successfully: {output_pdf_path}")

def create_single_card_pdf(svg_file_path, output_pdf_path):
    """
    Create a PDF with a single business card centered on A4 page
    """
    page_width, page_height = A4
    
    # Read SVG content
    with open(svg_file_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    # Convert SVG to PNG
    png_data = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'))
    
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
    
    # Save PNG temporarily
    temp_png_path = "temp_single_card.png"
    with open(temp_png_path, 'wb') as temp_file:
        temp_file.write(png_data)
    
    # Draw the card
    c.drawImage(temp_png_path, x, y, width=card_width, height=card_height)
    
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
    
    # Clean up
    if os.path.exists(temp_png_path):
        os.remove(temp_png_path)
    
    c.save()
    print(f"Single card PDF saved: {output_pdf_path}")

def main():
    # File paths
    script_dir = Path(__file__).parent
    svg_file = script_dir / "business_card_print_ready.svg"
    
    if not svg_file.exists():
        print(f"Error: SVG file not found: {svg_file}")
        return
    
    # Create both versions
    print("Creating business card PDFs...\n")
    
    # Multiple cards per page
    multiple_pdf = script_dir / "business_cards_multiple_A4.pdf"
    svg_to_pdf_a4(str(svg_file), str(multiple_pdf))
    
    print()
    
    # Single card centered
    single_pdf = script_dir / "business_card_single_A4.pdf"
    create_single_card_pdf(str(svg_file), str(single_pdf))
    
    print(f"\nConversion complete!")
    print(f"Files created:")
    print(f"  1. {multiple_pdf.name} - Multiple cards per A4 page")
    print(f"  2. {single_pdf.name} - Single card centered on A4")
    print(f"\nReady for printing!")

if __name__ == "__main__":
    main()
