# 🎨 How to Install and Use the GIMP Script

## � **IMPORTANT: GIMP Version Compatibility**

### **For GIMP 3.0 Users:**
- Use the file: `ide_business_card_gimp3_script.scm` (GIMP 3.0 compatible)
- Scripts folder: `GIMP\3.0\scripts\`

### **For GIMP 2.10 Users:**
- Use the file: `ide_business_card_gimp_script.scm` (GIMP 2.10 compatible)
- Scripts folder: `GIMP\2.10\scripts\`

## �📋 Step-by-Step Installation Guide

### 1. **Locate Your GIMP Scripts Folder**

**GIMP 3.0 - Windows:**
```
C:\Users\[YourUsername]\AppData\Roaming\GIMP\3.0\scripts\
```

**GIMP 3.0 - macOS:**
```
~/Library/Application Support/GIMP/3.0/scripts/
```

**GIMP 3.0 - Linux:**
```
~/.config/GIMP/3.0/scripts/
```

**GIMP 2.10 - Windows:**
```
C:\Users\[YourUsername]\AppData\Roaming\GIMP\2.10\scripts\
```

**GIMP 2.10 - macOS:**
```
~/Library/Application Support/GIMP/2.10/scripts/
```

**GIMP 2.10 - Linux:**
```
~/.gimp-2.10/scripts/
```

**Alternative Method (Any OS):**
1. Open GIMP
2. Go to **Edit > Preferences**
3. Click on **Folders > Scripts**
4. You'll see the script folder path listed

### 2. **Copy the Correct Script File**

**For GIMP 3.0:**
1. **Copy** the file `ide_business_card_gimp3_script.scm`
2. **Paste** it into your GIMP 3.0 scripts folder
3. **Ensure** the file has the `.scm` extension

**For GIMP 2.10:**
1. **Copy** the file `ide_business_card_gimp_script.scm`
2. **Paste** it into your GIMP 2.10 scripts folder
3. **Ensure** the file has the `.scm` extension

### 3. **Refresh GIMP Scripts**

**Option A - Restart GIMP:**
- Close GIMP completely
- Reopen GIMP

**Option B - Refresh Scripts (Faster):**
1. In GIMP, go to **Filters**
2. Click **Script-Fu**
3. Click **Refresh Scripts**

## 🚀 How to Run the Script

### **Method 1: From Menu**
1. Open GIMP
2. Go to **Filters** → **Generic**
3. Look for **"IDE Business Card Template (GIMP 3.0)"** or **"IDE Business Card Template"**
4. Click on it

### **Method 2: From Script-Fu Console**
**GIMP 3.0:**
1. Go to **Filters** → **Script-Fu** → **Console**
2. Type: `(script-fu-create-ide-business-card)`
3. Press **Enter**

**GIMP 2.10:**
1. Go to **Filters** → **Script-Fu** → **Console**
2. Type: `(create-ide-business-card-template)`
3. Press **Enter**

## ✨ What the Script Creates

When you run the script, it will automatically create:

### 🎯 **New Image (1003 x 1003 pixels)**
- **Resolution**: 300 DPI (print quality)
- **Size**: 85mm x 85mm square
- **Color Mode**: RGB

### 📁 **Layers Created:**
1. **IDE Front Layer** - VS Code style JSON interface
2. **Terminal Back Layer** - Terminal with QR code area
3. **Multiple Text Layers** - All the contact information
4. **Background Elements** - Windows, borders, status bars

## 🛠️ Customizing After Creation

### **Editing Text:**
1. **Select** any text layer in the Layers panel
2. **Double-click** the text layer
3. **Edit** the text content
4. **Change** font, size, or color as needed

### **Adding Your Photo:**
1. **File** → **Open as Layers**
2. **Select** your photo
3. **Scale** and **position** it appropriately
4. **Place** it in the designated area

### **Replacing QR Code:**
1. **Generate** a real QR code (use the `qr_code_website.png` we created)
2. **File** → **Open as Layers**
3. **Position** it in the white QR area
4. **Scale** to fit properly

### **Adjusting Colors:**
1. **Select** the layer you want to change
2. **Colors** → **Hue-Saturation** or **Color Balance**
3. **Adjust** to your preference

## 🖨️ Preparing for Print

### **Export Options:**
1. **File** → **Export As**
2. **Choose format:**
   - **PDF** (best for printing)
   - **PNG** (high quality, 300 DPI)
   - **TIFF** (professional printing)

### **Print Settings:**
1. **Image** → **Print Size**
2. **Set to:** 85mm x 85mm
3. **Resolution:** 300 DPI
4. **Export** with these settings

## ❗ Troubleshooting

### **Script Not Appearing in Menu:**
1. **Check** file is in correct scripts folder (3.0 vs 2.10)
2. **Use correct script file** for your GIMP version
3. **Ensure** file extension is `.scm`
4. **Restart** GIMP or refresh scripts
5. **Check** GIMP version compatibility

### **GIMP 3.0 Specific Issues:**
1. **Script-Fu changes**: GIMP 3.0 has updated Script-Fu syntax
2. **Use GIMP 3.0 script**: Make sure you're using `ide_business_card_gimp3_script.scm`
3. **Different menu structure**: Some menu locations may have changed
4. **Console commands**: Use `script-fu-create-ide-business-card` for GIMP 3.0

### **Script Error When Running:**
1. **Close** any open images in GIMP
2. **Try** running script with fresh GIMP session
3. **Check** GIMP console for error messages

### **Text Overlapping Issues:**
1. **Select** overlapping text layers
2. **Move** them using the Move tool
3. **Adjust** font size if needed
4. **Use** Text tool to edit positioning

### **Colors Look Different:**
1. **Check** your monitor color profile
2. **Use** View → Proof Colors for print preview
3. **Convert** to CMYK before final printing

## 🎨 Advanced Customization

### **Creating Variations:**
1. **Duplicate** layers for different versions
2. **Change** text content for different contacts
3. **Save** as XCF file to preserve layers
4. **Export** multiple versions

### **Adding Effects:**
1. **Drop Shadow:** Filters → Light and Shadow → Drop Shadow
2. **Glow Effect:** Filters → Light and Shadow → Glow
3. **Gradients:** Use Gradient tool on background

### **Professional Tips:**
1. **Keep** original XCF file for future edits
2. **Use** guides for precise alignment
3. **Test print** on regular paper first
4. **Check** colors in different lighting

## 📞 Quick Reference

**GIMP 3.0:**
- **File:** `ide_business_card_gimp3_script.scm`
- **Menu Path:** Filters → Generic → IDE Business Card Template (GIMP 3.0)
- **Console Command:** `(script-fu-create-ide-business-card)`

**GIMP 2.10:**
- **File:** `ide_business_card_gimp_script.scm`
- **Menu Path:** Filters → Generic → IDE Business Card Template
- **Console Command:** `(create-ide-business-card-template)`

**Output Size:** 1003 x 1003 pixels (85mm x 85mm at 300 DPI)  
**Layers:** Front IDE + Back Terminal + Text elements  

## 🎯 Final Steps

1. **Install** script in GIMP scripts folder
2. **Restart** GIMP or refresh scripts
3. **Run** script from Filters → Generic menu
4. **Customize** text and images as needed
5. **Export** for printing at 300 DPI

Your professional IDE-style business cards will be ready to print! 🚀
