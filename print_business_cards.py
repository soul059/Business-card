#!/usr/bin/env python3
"""
Simple PDF creator using browser's print-to-PDF
Opens HTML files in browser for manual PDF creation
"""

import webbrowser
import os
import time
from pathlib import Path

def open_files_for_printing():
    """Open HTML files in default browser for printing"""
    script_dir = Path(__file__).parent
    
    html_files = [
        ("business_cards_multiple_A4.html", "Multiple cards per page (10 cards)"),
        ("business_cards_single_A4.html", "Single card centered")
    ]
    
    print("Opening business card files for printing...\n")
    
    for filename, description in html_files:
        file_path = script_dir / filename
        if file_path.exists():
            print(f"Opening: {description}")
            print(f"File: {filename}")
            
            # Convert to file:// URL for browser
            file_url = f"file:///{file_path.resolve()}"
            webbrowser.open(file_url)
            
            time.sleep(2)  # Small delay between opening files
            print("✓ Opened in browser\n")
        else:
            print(f"❌ File not found: {filename}\n")
    
    print("="*60)
    print("PRINTING INSTRUCTIONS:")
    print("="*60)
    print("1. Both files should now be open in your web browser")
    print("2. In each browser tab, press Ctrl+P to print")
    print("3. Choose 'Save as PDF' as the destination OR select your printer")
    print("4. Set paper size to A4")
    print("5. In 'More settings':")
    print("   - Enable 'Background graphics'")
    print("   - Set margins to 'Minimum' or 'Custom' (10mm)")
    print("6. Click 'Print' or 'Save'")
    print("\nFILE DESCRIPTIONS:")
    print("- Multiple cards: 10 business cards per A4 page (economical)")
    print("- Single card: 1 business card centered on A4 (preview/template)")
    print("\nPRINTING TIPS:")
    print("- Use 250-300gsm cardstock for professional results")
    print("- Print at highest quality settings")
    print("- Cut along dashed lines")
    print("- Each card is 85mm × 55mm (standard business card size)")
    print("- The design shows front and back side by side")

def main():
    script_dir = Path(__file__).parent
    
    # Check if we're in the right directory
    svg_file = script_dir / "business_card_print_ready.svg"
    if not svg_file.exists():
        print("Error: This script should be run from the business card directory")
        print("Make sure business_card_print_ready.svg is in the same folder")
        return
    
    # Check if HTML files exist
    html_multiple = script_dir / "business_cards_multiple_A4.html"
    html_single = script_dir / "business_cards_single_A4.html"
    
    if not html_multiple.exists() or not html_single.exists():
        print("HTML files not found. Creating them now...")
        try:
            # Import and run the HTML creator
            import subprocess
            subprocess.run([
                "python", 
                str(script_dir / "svg_to_pdf_simple.py")
            ], check=True)
        except:
            print("Please run 'svg_to_pdf_simple.py' first to create the HTML files")
            return
    
    open_files_for_printing()

if __name__ == "__main__":
    main()
