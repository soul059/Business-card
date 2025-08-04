@echo off
echo Opening all business card PDF layouts for comparison...
echo.

echo Opening layouts:
echo - 10 cards (2x5) - Most economical
start "" "business_cards_2x5_A4.pdf"

timeout /t 1 /nobreak >nul

echo - 9 cards (3x3) - Square grid
start "" "business_cards_3x3_A4.pdf"

timeout /t 1 /nobreak >nul

echo - 8 cards (2x4) - Good spacing
start "" "business_cards_2x4_A4.pdf"

timeout /t 1 /nobreak >nul

echo - 6 cards (2x3) - Small batch
start "" "business_cards_2x3_A4.pdf"

timeout /t 1 /nobreak >nul

echo - 6 cards (1x6) - Single column
start "" "business_cards_1x6_A4.pdf"

timeout /t 1 /nobreak >nul

echo - 4 cards (1x4) - Large spacing
start "" "business_cards_1x4_A4.pdf"

timeout /t 1 /nobreak >nul

echo - 1 card - Preview
start "" "business_cards_single_A4.pdf"

echo.
echo All PDF layouts opened!
echo.
echo LAYOUT GUIDE:
echo =============
echo 10 cards (2x5) - Best for mass printing, most economical
echo  9 cards (3x3) - Square layout, easy cutting grid
echo  8 cards (2x4) - Good balance of quantity and spacing
echo  6 cards (2x3) - Small batch, less waste
echo  6 cards (1x6) - Single column, easiest cutting
echo  4 cards (1x4) - Large spacing, best quality control
echo  1 card       - Preview and testing
echo.
echo Choose the layout that best fits your needs!
echo See MULTIPLE_CARDS_GUIDE.md for detailed instructions.
echo.
pause
