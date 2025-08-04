#!/usr/bin/env python3
"""
Customizable Square Business Card P        .card svg {
            width: 100%;
            height: 100%;
            max-width: 85mm;
            max-height: 85mm;
            object-fit: contain;
        }erator
Create PDFs with different numbers of square cards per page
"""

import sys
from pathlib import Path

def create_custom_layout_html(svg_file_path, cards_horizontal=2, cards_vertical=3, output_html_path=None):
    """Create HTML with custom card layout"""
    
    # Read the SVG content
    with open(svg_file_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    cards_per_page = cards_horizontal * cards_vertical
    
    if output_html_path is None:
        output_html_path = f"business_cards_{cards_horizontal}x{cards_vertical}_A4.html"
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Business Cards - {cards_horizontal}×{cards_vertical} Layout</title>
    <style>
        @page {{
            size: A4;
            margin: 8mm;
        }}
        
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        
        .page-title {{
            text-align: center;
            font-size: 12pt;
            font-weight: bold;
            margin-bottom: 3mm;
        }}
        
        .cards-container {{
            display: grid;
            grid-template-columns: repeat({cards_horizontal}, 1fr);
            grid-template-rows: repeat({cards_vertical}, 1fr);
            gap: 1.5mm;
            height: calc(100vh - 25mm);
            margin-bottom: 3mm;
        }}
        
        .card {{
            border: 0.5px dashed #999;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            background: white;
        }}
        
        .card svg {{
            width: 100%;
            height: 100%;
            max-width: 85mm;
            max-height: 55mm;
        }}
        
        .instructions {{
            font-size: 7pt;
            color: #666;
            line-height: 1.2;
        }}
        
        .instructions ul {{
            margin: 1mm 0;
            padding-left: 12px;
        }}
        
        .instructions li {{
            margin: 0.5mm 0;
        }}
        
        @media print {{
            .page-title {{ 
                font-size: 10pt; 
                margin-bottom: 2mm;
            }}
            .instructions {{ 
                font-size: 6pt; 
            }}
        }}
    </style>
</head>
<body>
    <div class="page-title">Business Cards - {cards_horizontal}×{cards_vertical} Layout ({cards_per_page} cards per page)</div>
    
    <div class="cards-container">
"""
    
    # Add cards
    for i in range(cards_per_page):
        html_content += f'        <div class="card">\n{svg_content}\n        </div>\n'
    
    html_content += f"""
    </div>
    
    <div class="instructions">
        <strong>Layout:</strong> {cards_horizontal} columns × {cards_vertical} rows = {cards_per_page} cards per A4 page
        <br><strong>Card Size:</strong> 85mm × 85mm (square business card)
        <br><strong>Printing:</strong> Use 250-300gsm cardstock, high-quality settings, cut along dashed lines
        <br><strong>Note:</strong> Front and back are separate files - print each separately or combine as needed
    </div>
</body>
</html>
"""
    
    return html_content, output_html_path

def create_pdf_with_playwright_custom(html_content, output_pdf_path):
    """Convert HTML to PDF using Playwright"""
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Set HTML content
            page.set_content(html_content)
            
            # Generate PDF
            page.pdf(
                path=str(output_pdf_path),
                format='A4',
                margin={
                    'top': '8mm',
                    'bottom': '8mm', 
                    'left': '8mm',
                    'right': '8mm'
                },
                print_background=True
            )
            
            browser.close()
        
        return True
        
    except ImportError:
        print("Playwright not installed. Install with: pip install playwright")
        print("Then run: playwright install chromium")
        return False
    except Exception as e:
        print(f"PDF conversion failed: {e}")
        return False

def main():
    script_dir = Path(__file__).parent
    svg_file = script_dir / "business_card_print_ready.svg"
    
    if not svg_file.exists():
        print(f"Error: SVG file not found: {svg_file}")
        return
    
    print("Business Card PDF Generator")
    print("=" * 40)
    
    # Predefined layouts optimized for square cards (85mm × 85mm)
    layouts = [
        (2, 3, "Standard (6 cards) - Best fit for A4"),
        (2, 2, "Medium (4 cards) - Good spacing"),
        (1, 3, "Single column (3 cards) - Easy cutting"),
        (3, 2, "Wide (6 cards) - Horizontal layout"),
        (1, 2, "Large (2 cards) - Maximum size"),
        (2, 1, "Horizontal (2 cards) - Side by side"),
        (1, 1, "Single card - Preview/template")
    ]
    
    print("Available layouts:")
    for i, (h, v, desc) in enumerate(layouts, 1):
        print(f"  {i}. {h}×{v} - {desc}")
    
    print("  8. Custom layout")
    print("  9. Create all standard layouts")
    
    try:
        choice = input("\nSelect layout (1-9): ").strip()
        
        if choice == "9":
            # Create all standard layouts
            print("\nCreating all standard layouts...")
            for h, v, desc in layouts[:6]:  # Skip single card for this batch
                create_layout(script_dir, svg_file, h, v, desc)
            print("All layouts created!")
            
        elif choice == "8":
            # Custom layout
            h = int(input("Cards horizontally (1-4): "))
            v = int(input("Cards vertically (1-8): "))
            if h < 1 or h > 4 or v < 1 or v > 8:
                print("Invalid layout. Using 2×5 instead.")
                h, v = 2, 5
            create_layout(script_dir, svg_file, h, v, "Custom")
            
        elif choice.isdigit() and 1 <= int(choice) <= 7:
            # Selected layout
            h, v, desc = layouts[int(choice) - 1]
            create_layout(script_dir, svg_file, h, v, desc)
            
        else:
            print("Invalid choice. Using standard 2×5 layout.")
            create_layout(script_dir, svg_file, 2, 5, "Standard")
            
    except (ValueError, KeyboardInterrupt):
        print("\nUsing standard 2×5 layout.")
        create_layout(script_dir, svg_file, 2, 5, "Standard")

def create_layout(script_dir, svg_file, h, v, desc):
    """Create a specific layout"""
    print(f"\nCreating {h}×{v} layout ({desc})...")
    
    # Create HTML
    html_content, html_filename = create_custom_layout_html(str(svg_file), h, v)
    html_path = script_dir / html_filename
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ HTML created: {html_filename}")
    
    # Create PDF
    pdf_filename = html_filename.replace('.html', '.pdf')
    pdf_path = script_dir / pdf_filename
    
    if create_pdf_with_playwright_custom(html_content, str(pdf_path)):
        print(f"✓ PDF created: {pdf_filename}")
        print(f"  Cards per page: {h * v}")
        print(f"  File size optimized for A4 printing")
    else:
        print(f"✗ PDF creation failed, but HTML file is available")

if __name__ == "__main__":
    main()
