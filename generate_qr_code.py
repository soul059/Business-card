#!/usr/bin/env python3
"""
QR Code Generator for Business Card
Generates a QR code pointing to the website
"""

def create_qr_code():
    try:
        import qrcode
        from qrcode.image.svg import SvgPathImage
        
        # Your website URL
        website_url = "https://keval.live"  # Update this to your actual domain
        
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% of codewords can be restored
            box_size=10,
            border=4,
        )
        
        # Add data to QR code
        qr.add_data(website_url)
        qr.make(fit=True)
        
        # Create SVG image
        img_svg = qr.make_image(image_factory=SvgPathImage)
        img_svg.save("qr_code_website.svg")
        
        # Create PNG image
        img_png = qr.make_image(fill_color="black", back_color="white")
        img_png.save("qr_code_website.png")
        
        print(f"✅ QR Code generated successfully!")
        print(f"📱 QR Code points to: {website_url}")
        print(f"📁 Files created:")
        print(f"   - qr_code_website.svg (Vector format)")
        print(f"   - qr_code_website.png (Raster format)")
        print(f"\n📝 Instructions:")
        print(f"1. Test the QR code with your phone camera")
        print(f"2. Replace the QR placeholder in the business card back design")
        print(f"3. Ensure the QR code is large enough to scan (at least 1cm x 1cm)")
        
        return True
        
    except ImportError:
        print("❌ qrcode library not found. Installing...")
        return False

def install_qrcode_and_generate():
    """Install qrcode library and generate QR code"""
    import subprocess
    import sys
    
    try:
        # Install qrcode library
        subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]"])
        print("✅ qrcode library installed successfully!")
        
        # Now try to generate QR code
        return create_qr_code()
        
    except Exception as e:
        print(f"❌ Error installing qrcode library: {e}")
        print("\n📝 Manual installation:")
        print("Run: pip install qrcode[pil]")
        print("Then run this script again")
        return False

if __name__ == "__main__":
    print("🔄 Generating QR Code for business card...")
    
    success = create_qr_code()
    
    if not success:
        print("\n🔄 Attempting to install qrcode library...")
        install_qrcode_and_generate()
