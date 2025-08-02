; Simple GIMP 3.0 Test Script
(define (script-fu-test-gimp3)
  (let* (
    (img (car (gimp-image-new 1003 1003 RGB)))
    (layer (car (gimp-layer-new img "Test Layer" 1003 1003 RGB-IMAGE 100 LAYER-MODE-NORMAL)))
    )
    
    ; Add layer to image
    (gimp-image-insert-layer img layer 0 0)
    
    ; Set resolution
    (gimp-image-set-resolution img 300 300)
    
    ; Fill with color
    (gimp-context-set-foreground '(30 30 48))
    (gimp-drawable-fill layer FILL-FOREGROUND)
    
    ; Display the image
    (gimp-display-new img)
    
    ; Return the image
    img
  )
)

; Register the test script
(script-fu-register
  "script-fu-test-gimp3"
  "Test GIMP 3.0 Script"
  "Simple test for GIMP 3.0 compatibility"
  "Assistant"
  "GPL"
  "2025"
  ""
)

(script-fu-menu-register "script-fu-test-gimp3" "<Image>/Filters/Generic")
