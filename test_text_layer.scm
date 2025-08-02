; GIMP 3.0 Minimal Script-Fu for Testing Text Layer Creation
; This script tests adding a single text layer with the fallback font "Sans"

(define (script-fu-test-text-layer)
  (let* (
    ; Create a new image
    (img (car (gimp-image-new 500 500 RGB)))
    ; Set the fallback font
    (font "Sans")
    )
    
    ; Create a new text layer
    (let* ((text-layer (car (gimp-text-layer-new img "Test Text" 50 PIXELS font))))
      ; Set the text color
      (gimp-text-layer-set-color text-layer '(255 255 255))
      ; Position the text layer
      (gimp-layer-set-offsets text-layer 100 100)
      ; Add the text layer to the image
      (gimp-image-insert-layer img text-layer 0 0))
    
    ; Display the image
    (gimp-display-new img)))

; Register the script for GIMP 3.0
(script-fu-register
  "script-fu-test-text-layer"
  "Test Text Layer Creation (GIMP 3.0)"
  "Minimal script to test text layer creation with fallback font"
  "Assistant"
  "GPL"
  "2025"
  ""
)

(script-fu-menu-register "script-fu-test-text-layer" "<Image>/Filters/Generic")
