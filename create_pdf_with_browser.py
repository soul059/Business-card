#!/usr/bin/env python3
"""
Browser-based PDF Converter for Business Cards
Uses playwright to convert HTML to PDF via Chrome/Edge browser
"""

import sys
from pathlib import Path

def create_pdf_with_playwright():
    """Use playwright to convert HTML to PDF"""
    try:
        from playwright.sync_api import sync_playwright
        
        script_dir = Path(__file__).parent
        html_files = [
            (script_dir / "business_cards_multiple_A4.html", script_dir / "business_cards_multiple_A4.pdf"),
            (script_dir / "business_cards_single_A4.html", script_dir / "business_cards_single_A4.pdf")
        ]
        
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch()
            page = browser.new_page()
            
            for html_file, pdf_file in html_files:
                if html_file.exists():
                    print(f"Converting {html_file.name} to PDF...")
                    
                    # Load HTML file
                    page.goto(f"file:///{html_file.resolve()}")
                    
                    # Generate PDF
                    page.pdf(
                        path=str(pdf_file),
                        format='A4',
                        margin={
                            'top': '10mm',
                            'bottom': '10mm', 
                            'left': '10mm',
                            'right': '10mm'
                        },
                        print_background=True
                    )
                    
                    print(f"PDF created: {pdf_file.name}")
            
            browser.close()
        
        return True
        
    except ImportError:
        print("Playwright not installed. Install with: pip install playwright")
        print("Then run: playwright install chromium")
        return False
    except Exception as e:
        print(f"Playwright conversion failed: {e}")
        return False

def install_playwright():
    """Install playwright and browser"""
    import subprocess
    import sys
    
    try:
        print("Installing playwright...")
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
        
        print("Installing chromium browser...")
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
        return False

def main():
    script_dir = Path(__file__).parent
    
    # Check if HTML files exist
    html_multiple = script_dir / "business_cards_multiple_A4.html"
    html_single = script_dir / "business_cards_single_A4.html"
    
    if not html_multiple.exists() or not html_single.exists():
        print("HTML files not found. Run svg_to_pdf_simple.py first.")
        return
    
    print("Attempting to create PDFs using browser automation...")
    
    # Try to convert with playwright
    if not create_pdf_with_playwright():
        print("\nWould you like to install playwright for PDF conversion? (y/n): ", end="")
        try:
            response = input().lower().strip()
            if response in ['y', 'yes']:
                if install_playwright():
                    print("\nTrying PDF conversion again...")
                    create_pdf_with_playwright()
                else:
                    print("Installation failed. Please install manually:")
                    print("pip install playwright")
                    print("playwright install chromium")
        except (EOFError, KeyboardInterrupt):
            print("\nSkipping playwright installation.")
    
    print("\nAlternative: Use the HTML files for printing:")
    print(f"1. Open {html_multiple.name} in a web browser")
    print(f"2. Open {html_single.name} in a web browser") 
    print("3. Press Ctrl+P and print to PDF or directly to printer")

if __name__ == "__main__":
    main()
