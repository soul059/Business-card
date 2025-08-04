#!/usr/bin/env python3
"""
Square Business Card PDF Generator
Create PDFs with multiple square cards per page (85mm × 85mm)
Works with separate front and back SVG files
"""

import sys
from pathlib import Path

def create_square_card_pdf(svg_file_path, cards_horizontal=2, cards_vertical=3, card_type="front"):
    """Create PDF layout optimized for square business cards"""
    
    # Read the SVG content
    with open(svg_file_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    cards_per_page = cards_horizontal * cards_vertical
    output_filename = f"square_cards_{card_type}_{cards_horizontal}x{cards_vertical}_A4"
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Square Business Cards - {card_type.title()} ({cards_horizontal}×{cards_vertical})</title>
    <style>
        @page {{
            size: A4;
            margin: 6mm;
        }}
        
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        
        .page-title {{
            text-align: center;
            font-size: 11pt;
            font-weight: bold;
            margin-bottom: 2mm;
            color: #333;
        }}
        
        .cards-container {{
            display: grid;
            grid-template-columns: repeat({cards_horizontal}, 1fr);
            grid-template-rows: repeat({cards_vertical}, 1fr);
            gap: 2mm;
            height: calc(100vh - 20mm);
            margin-bottom: 2mm;
        }}
        
        .card {{
            border: 1px dashed #666;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            background: white;
            aspect-ratio: 1;
            max-width: 85mm;
            max-height: 85mm;
        }}
        
        .card svg {{
            width: 100%;
            height: 100%;
            max-width: 85mm;
            max-height: 85mm;
            object-fit: contain;
        }}
        
        .instructions {{
            font-size: 7pt;
            color: #555;
            line-height: 1.3;
            text-align: center;
        }}
        
        .cut-guides {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            z-index: -1;
        }}
        
        @media print {{
            .page-title {{ 
                font-size: 9pt; 
                margin-bottom: 1mm;
            }}
            .instructions {{ 
                font-size: 6pt; 
            }}
        }}
    </style>
</head>
<body>
    <div class="page-title">Square Business Cards - {card_type.title()} Side ({cards_horizontal}×{cards_vertical} = {cards_per_page} cards)</div>
    
    <div class="cards-container">
"""
    
    # Add cards
    for i in range(cards_per_page):
        html_content += f'        <div class="card">\n{svg_content}\n        </div>\n'
    
    html_content += f"""
    </div>
    
    <div class="instructions">
        <strong>Square Business Cards (85mm × 85mm)</strong><br>
        Card Type: {card_type.title()} • Layout: {cards_horizontal} cols × {cards_vertical} rows<br>
        Print on 250-300gsm cardstock • Cut along dashed lines • High quality settings recommended
    </div>
</body>
</html>
"""
    
    return html_content, output_filename

def create_pdf_with_playwright(html_content, output_pdf_path):
    """Convert HTML to PDF using Playwright"""
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Set HTML content
            page.set_content(html_content)
            
            # Generate PDF with optimized settings for square cards
            page.pdf(
                path=str(output_pdf_path),
                format='A4',
                margin={
                    'top': '6mm',
                    'bottom': '6mm', 
                    'left': '6mm',
                    'right': '6mm'
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
    front_svg = script_dir / "business_card_front.svg"
    back_svg = script_dir / "business_card_back.svg"
    
    # Check if square card files exist
    if not front_svg.exists() or not back_svg.exists():
        print("Error: Square business card SVG files not found!")
        print(f"Looking for: {front_svg} and {back_svg}")
        return
    
    print("Square Business Card PDF Generator")
    print("=" * 45)
    print("Optimized layouts for 85mm × 85mm square cards")
    print()
    
    # Optimal layouts for square cards on A4
    layouts = [
        (2, 3, "Standard (6 cards) - Best fit"),
        (2, 2, "Medium (4 cards) - Good spacing"),
        (1, 3, "Column (3 cards) - Easy cutting"),
        (3, 2, "Wide (6 cards) - Horizontal"),
        (1, 2, "Large (2 cards) - Maximum size"),
        (2, 1, "Side-by-side (2 cards)"),
        (1, 1, "Single card - Preview")
    ]
    
    print("Available layouts:")
    for i, (h, v, desc) in enumerate(layouts, 1):
        print(f"  {i}. {h}×{v} - {desc}")
    
    print("  8. Custom layout")
    print("  9. Create all layouts (both front and back)")
    print("  f. Front cards only")
    print("  b. Back cards only")
    
    try:
        choice = input("\nSelect option: ").strip().lower()
        
        if choice == "9":
            # Create all layouts for both front and back
            print("\nCreating all layouts for both front and back...")
            for h, v, desc in layouts[:6]:  # Skip single card for batch
                create_card_layout(script_dir, front_svg, back_svg, h, v, desc, both=True)
            print("All layouts created!")
            
        elif choice == "f":
            # Front cards only
            layout_choice = input("Select layout (1-7): ").strip()
            if layout_choice.isdigit() and 1 <= int(layout_choice) <= 7:
                h, v, desc = layouts[int(layout_choice) - 1]
                create_card_layout(script_dir, front_svg, back_svg, h, v, desc, front_only=True)
            
        elif choice == "b":
            # Back cards only
            layout_choice = input("Select layout (1-7): ").strip()
            if layout_choice.isdigit() and 1 <= int(layout_choice) <= 7:
                h, v, desc = layouts[int(layout_choice) - 1]
                create_card_layout(script_dir, front_svg, back_svg, h, v, desc, back_only=True)
            
        elif choice == "8":
            # Custom layout
            h = int(input("Cards horizontally (1-3): "))
            v = int(input("Cards vertically (1-4): "))
            side = input("Front (f), Back (b), or Both (enter): ").strip().lower()
            
            if h < 1 or h > 3 or v < 1 or v > 4:
                print("Invalid layout. Using 2×3 instead.")
                h, v = 2, 3
            
            if side == "f":
                create_card_layout(script_dir, front_svg, back_svg, h, v, "Custom", front_only=True)
            elif side == "b":
                create_card_layout(script_dir, front_svg, back_svg, h, v, "Custom", back_only=True)
            else:
                create_card_layout(script_dir, front_svg, back_svg, h, v, "Custom", both=True)
            
        elif choice.isdigit() and 1 <= int(choice) <= 7:
            # Selected layout for both sides
            h, v, desc = layouts[int(choice) - 1]
            create_card_layout(script_dir, front_svg, back_svg, h, v, desc, both=True)
            
        else:
            print("Invalid choice. Using standard 2×3 layout for both sides.")
            create_card_layout(script_dir, front_svg, back_svg, 2, 3, "Standard", both=True)
            
    except (ValueError, KeyboardInterrupt):
        print("\nUsing standard 2×3 layout for both sides.")
        create_card_layout(script_dir, front_svg, back_svg, 2, 3, "Standard", both=True)

def create_card_layout(script_dir, front_svg, back_svg, h, v, desc, both=False, front_only=False, back_only=False):
    """Create layouts for square business cards"""
    print(f"\nCreating {h}×{v} layout ({desc})...")
    
    if both or front_only:
        # Create front layout
        html_content, filename = create_square_card_pdf(str(front_svg), h, v, "front")
        html_path = script_dir / f"{filename}.html"
        pdf_path = script_dir / f"{filename}.pdf"
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        if create_pdf_with_playwright(html_content, str(pdf_path)):
            print(f"✓ Front cards PDF: {filename}.pdf ({h * v} cards)")
        else:
            print(f"✗ Front PDF failed, HTML available: {filename}.html")
    
    if both or back_only:
        # Create back layout
        html_content, filename = create_square_card_pdf(str(back_svg), h, v, "back")
        html_path = script_dir / f"{filename}.html"
        pdf_path = script_dir / f"{filename}.pdf"
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        if create_pdf_with_playwright(html_content, str(pdf_path)):
            print(f"✓ Back cards PDF: {filename}.pdf ({h * v} cards)")
        else:
            print(f"✗ Back PDF failed, HTML available: {filename}.html")

if __name__ == "__main__":
    main()
