#!/usr/bin/env python3
"""
Simple SVG to PDF Converter for Business Cards
Uses WeasyPrint for reliable SVG to PDF conversion
"""

import os
import sys
from pathlib import Path

def create_html_wrapper(svg_file_path, cards_per_page=10):
    """Create an HTML file that embeds the SVG for PDF conversion"""
    
    # Read the SVG content
    with open(svg_file_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    # Calculate layout
    cards_horizontal = 2  # 2 cards horizontally on A4
    cards_vertical = 5    # 5 cards vertically on A4
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Business Cards - Print Ready</title>
    <style>
        @page {{
            size: A4;
            margin: 10mm;
        }}
        
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        
        .page-title {{
            text-align: center;
            font-size: 14pt;
            font-weight: bold;
            margin-bottom: 5mm;
        }}
        
        .cards-container {{
            display: grid;
            grid-template-columns: repeat({cards_horizontal}, 1fr);
            grid-template-rows: repeat({cards_vertical}, 1fr);
            gap: 2mm;
            height: calc(100vh - 20mm);
        }}
        
        .card {{
            border: 1px dashed #ccc;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }}
        
        .card svg {{
            width: 100%;
            height: 100%;
            max-width: 85mm;
            max-height: 55mm;
        }}
        
        .instructions {{
            margin-top: 5mm;
            font-size: 8pt;
            color: #666;
        }}
        
        .instructions ul {{
            margin: 0;
            padding-left: 15px;
        }}
        
        .single-card {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: calc(100vh - 40mm);
        }}
        
        .single-card svg {{
            width: 85mm;
            height: 55mm;
            border: 2px dashed #999;
        }}
        
        .measurements {{
            font-size: 8pt;
            color: #333;
            text-align: center;
            margin-top: 10mm;
        }}
    </style>
</head>
<body>
    <div class="page-title">Business Cards - Print Template ({cards_horizontal} × {cards_vertical} = {cards_horizontal * cards_vertical} cards per page)</div>
    
    <div class="cards-container">
"""
    
    # Add multiple cards
    for i in range(cards_horizontal * cards_vertical):
        html_content += f'        <div class="card">\n{svg_content}\n        </div>\n'
    
    html_content += """
    </div>
    
    <div class="instructions">
        <strong>Printing Instructions:</strong>
        <ul>
            <li>Print on 250-300gsm cardstock for best results</li>
            <li>Use high-quality/photo printing settings</li>
            <li>Cut along the dashed lines</li>
            <li>Each card measures 85mm × 55mm (standard business card size)</li>
            <li>The design shows both front and back side by side - cut in the middle to separate</li>
        </ul>
    </div>
</body>
</html>
"""
    
    return html_content

def create_single_card_html(svg_file_path):
    """Create HTML for a single centered card"""
    
    with open(svg_file_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Business Card - Single Print Template</title>
    <style>
        @page {{
            size: A4;
            margin: 15mm;
        }}
        
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        
        .page-title {{
            text-align: center;
            font-size: 16pt;
            font-weight: bold;
            margin-bottom: 10mm;
        }}
        
        .single-card {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 60mm;
            margin: 20mm 0;
        }}
        
        .card-container {{
            position: relative;
            border: 2px dashed #999;
            padding: 2mm;
        }}
        
        .card-container svg {{
            width: 85mm;
            height: 55mm;
            display: block;
        }}
        
        .measurements {{
            font-size: 10pt;
            color: #333;
            text-align: center;
            margin: 10mm 0;
        }}
        
        .instructions {{
            margin-top: 15mm;
            font-size: 10pt;
            color: #666;
        }}
        
        .instructions ul {{
            margin: 5mm 0;
            padding-left: 20px;
        }}
    </style>
</head>
<body>
    <div class="page-title">Business Card - Print Template</div>
    
    <div class="single-card">
        <div class="card-container">
            {svg_content}
        </div>
    </div>
    
    <div class="measurements">
        <strong>Card Size: 85mm × 55mm (Standard Business Card)</strong>
    </div>
    
    <div class="instructions">
        <strong>Printing Instructions:</strong>
        <ul>
            <li>Print on high-quality cardstock (250-300gsm recommended)</li>
            <li>Use highest quality print settings</li>
            <li>Cut carefully along the dashed lines</li>
            <li>Standard business card size: 85mm × 55mm</li>
            <li>The card contains both front and back designs side by side</li>
            <li>Cut vertically in the middle to separate front and back</li>
        </ul>
        
        <strong>Alternative Methods:</strong>
        <ul>
            <li>Open the SVG file directly in a web browser and print</li>
            <li>Use online SVG to PDF converters (CloudConvert, Convertio)</li>
            <li>Import into design software (Adobe Illustrator, Inkscape)</li>
        </ul>
    </div>
</body>
</html>
"""
    
    return html_content

def convert_with_weasyprint(html_content, output_pdf_path):
    """Convert HTML to PDF using WeasyPrint"""
    try:
        import weasyprint
        
        print(f"Converting to PDF: {output_pdf_path}")
        
        # Convert HTML to PDF
        html_doc = weasyprint.HTML(string=html_content)
        html_doc.write_pdf(output_pdf_path)
        
        print(f"PDF created successfully: {output_pdf_path}")
        return True
        
    except Exception as e:
        print(f"WeasyPrint conversion failed: {e}")
        return False

def create_browser_printable_html(svg_file_path, output_html_path, card_type="multiple"):
    """Create an HTML file that can be printed directly from a browser"""
    
    if card_type == "single":
        html_content = create_single_card_html(svg_file_path)
    else:
        html_content = create_html_wrapper(svg_file_path)
    
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML file created: {output_html_path}")
    print(f"You can open this file in a web browser and print it (Ctrl+P)")
    return True

def main():
    # File paths
    script_dir = Path(__file__).parent
    svg_file = script_dir / "business_card_print_ready.svg"
    
    if not svg_file.exists():
        print(f"Error: SVG file not found: {svg_file}")
        return
    
    print("Creating business card print files...\n")
    
    success_count = 0
    
    # Create HTML files (always works)
    html_multiple = script_dir / "business_cards_multiple_A4.html"
    if create_browser_printable_html(str(svg_file), str(html_multiple), "multiple"):
        success_count += 1
    
    html_single = script_dir / "business_cards_single_A4.html"
    if create_browser_printable_html(str(svg_file), str(html_single), "single"):
        success_count += 1
    
    print()
    
    # Try WeasyPrint conversion
    try:
        # Multiple cards PDF
        pdf_multiple = script_dir / "business_cards_multiple_A4.pdf"
        html_content_multiple = create_html_wrapper(str(svg_file))
        if convert_with_weasyprint(html_content_multiple, str(pdf_multiple)):
            success_count += 1
        
        # Single card PDF
        pdf_single = script_dir / "business_cards_single_A4.pdf"
        html_content_single = create_single_card_html(str(svg_file))
        if convert_with_weasyprint(html_content_single, str(pdf_single)):
            success_count += 1
            
    except ImportError:
        print("WeasyPrint not available - using HTML files only")
    except Exception as e:
        print(f"PDF conversion had issues: {e}")
    
    print(f"\n{'='*50}")
    print(f"Conversion complete! Created {success_count} files:")
    print(f"{'='*50}")
    
    # List created files
    files_created = []
    for file_path in [
        script_dir / "business_cards_multiple_A4.html",
        script_dir / "business_cards_single_A4.html", 
        script_dir / "business_cards_multiple_A4.pdf",
        script_dir / "business_cards_single_A4.pdf"
    ]:
        if file_path.exists():
            files_created.append(file_path.name)
    
    for i, filename in enumerate(files_created, 1):
        print(f"  {i}. {filename}")
    
    print(f"\nHow to print:")
    print(f"1. For PDF files: Open in Adobe Reader/browser and print")
    print(f"2. For HTML files: Open in web browser (Chrome/Firefox/Edge)")
    print(f"   - Press Ctrl+P to print")
    print(f"   - Set paper size to A4")
    print(f"   - Choose 'More settings' > 'Background graphics' enabled")
    print(f"   - Print on cardstock (250-300gsm) for best results")

if __name__ == "__main__":
    main()
