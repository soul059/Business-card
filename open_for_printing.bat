@echo off
echo Opening business card HTML files for printing...
echo.

echo Opening multiple cards layout...
start "" "business_cards_multiple_A4.html"

timeout /t 2 /nobreak >nul

echo Opening single card layout...
start "" "business_cards_single_A4.html"

echo.
echo PRINTING INSTRUCTIONS:
echo =====================
echo 1. Both files should now be open in your web browser
echo 2. Press Ctrl+P in the browser to print
echo 3. Choose your printer or "Save as PDF"
echo 4. Set paper size to A4
echo 5. Enable "Background graphics" in print options
echo 6. For best results, use 250-300gsm cardstock
echo.
echo Multiple cards file: 10 business cards per A4 page
echo Single card file: 1 centered business card per A4 page
echo.
pause
