; GIMP 3.0 Compatible Script-Fu for IDE-Style Business Card Template
; Version 8: Forces fallback font "Sans" to avoid font issues

(define (script-fu-create-ide-business-card-v8)
  (let* (
    ; Convert mm to pixels at 300 DPI: 85mm = 1003 pixels
    (img-width 1003)
    (img-height 1003)
    (img (car (gimp-image-new img-width img-height RGB)))
    )
    
    ; Create layers
    (let* (
      (front-layer (car (gimp-layer-new img "IDE Front" img-width img-height RGB-IMAGE 100 LAYER-MODE-NORMAL)))
      (back-layer (car (gimp-layer-new img "Terminal Back" img-width img-height RGB-IMAGE 100 LAYER-MODE-NORMAL)))
      (ide-bg '(30 30 48))
      (editor-bg '(45 45 48))
      (accent-color '(0 122 204))
      (text-color '(212 212 212))
      (string-color '(206 145 120))
      (key-color '(156 220 254))
      (font "Sans") ; Use fallback font exclusively
      )
      
      ; Add layers to image
      (gimp-image-insert-layer img back-layer 0 0)
      (gimp-image-insert-layer img front-layer 0 0)
      
      ; Set resolution for print
      (gimp-image-set-resolution img 300 300)
      
      ; --- FRONT CARD ---
      
      ; Create front card background
      (gimp-context-set-foreground ide-bg)
      (gimp-drawable-fill front-layer FILL-FOREGROUND)
      
      ; Create IDE window border
      (gimp-context-set-foreground editor-bg)
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 24 24 955 955)
      (gimp-drawable-edit-fill front-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      ; Add window border
      (gimp-context-set-foreground accent-color)
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 24 24 955 4)
      (gimp-drawable-edit-fill front-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      ; Create line numbers background
      (gimp-context-set-foreground '(37 37 38))
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 24 94 94 885)
      (gimp-drawable-edit-fill front-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      ; Add tab
      (gimp-context-set-foreground ide-bg)
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 189 30 295 59)
      (gimp-drawable-edit-fill front-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      ; --- BACK CARD ---
      
      ; Create back card background
      (gimp-context-set-foreground ide-bg)
      (gimp-drawable-fill back-layer FILL-FOREGROUND)
      
      ; Create terminal window
      (gimp-context-set-foreground editor-bg)
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 24 24 955 955)
      (gimp-drawable-edit-fill back-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      ; Add terminal border
      (gimp-context-set-foreground accent-color)
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 24 24 955 4)
      (gimp-drawable-edit-fill back-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      ; Add QR code placeholder
      (gimp-context-set-foreground '(255 255 255))
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 259 425 484 484)
      (gimp-drawable-edit-fill back-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      (gimp-context-set-foreground '(0 0 0))
      (gimp-image-select-rectangle img CHANNEL-OP-REPLACE 277 443 448 448)
      (gimp-drawable-edit-fill back-layer FILL-FOREGROUND)
      (gimp-selection-none img)
      
      ; --- TEXT LAYERS ---
      
      ; File tab text
      (let* ((tab-text (car (gimp-text-layer-new img "developer.json" 29 PIXELS font))))
        (gimp-text-layer-set-color tab-text text-color)
        (gimp-layer-set-offsets tab-text 200 50)
        (gimp-image-insert-layer img tab-text 0 0))
      
      ; Line numbers
      (let ((line-num 1) (y-pos 142))
        (while (<= line-num 17)
          (let* ((num-text (car (gimp-text-layer-new img (number->string line-num) 29 PIXELS font))))
            (gimp-text-layer-set-color num-text '(133 133 133))
            (gimp-layer-set-offsets num-text 35 y-pos)
            (gimp-image-insert-layer img num-text 0 0))
          (set! line-num (+ line-num 1))
          (set! y-pos (+ y-pos 47))))
      
      ; JSON structure
      (let* ((open-brace (car (gimp-text-layer-new img "{" 33 PIXELS font))))
        (gimp-text-layer-set-color open-brace text-color)
        (gimp-layer-set-offsets open-brace 142 142)
        (gimp-image-insert-layer img open-brace 0 0))
      
      (let* ((name-key (car (gimp-text-layer-new img "\"name\":" 33 PIXELS font))))
        (gimp-text-layer-set-color name-key key-color)
        (gimp-layer-set-offsets name-key 165 189)
        (gimp-image-insert-layer img name-key 0 0))
      (let* ((name-value (car (gimp-text-layer-new img "\"Keval Chauhan\"," 33 PIXELS font))))
        (gimp-text-layer-set-color name-value string-color)
        (gimp-layer-set-offsets name-value 301 189)
        (gimp-image-insert-layer img name-value 0 0))
      
      (let* ((role-key (car (gimp-text-layer-new img "\"role\":" 33 PIXELS font))))
        (gimp-text-layer-set-color role-key key-color)
        (gimp-layer-set-offsets role-key 165 236)
        (gimp-image-insert-layer img role-key 0 0))
      (let* ((role-value (car (gimp-text-layer-new img "\"Web Developer\"," 33 PIXELS font))))
        (gimp-text-layer-set-color role-value string-color)
        (gimp-layer-set-offsets role-value 301 236)
        (gimp-image-insert-layer img role-value 0 0))
      
      (let* ((contact-key (car (gimp-text-layer-new img "\"contact\": {" 33 PIXELS font))))
        (gimp-text-layer-set-color contact-key key-color)
        (gimp-layer-set-offsets contact-key 165 283)
        (gimp-image-insert-layer img contact-key 0 0))
      
      (let* ((phone-key (car (gimp-text-layer-new img "\"phone\":" 33 PIXELS font))))
        (gimp-text-layer-set-color phone-key key-color)
        (gimp-layer-set-offsets phone-key 189 330)
        (gimp-image-insert-layer img phone-key 0 0))
      (let* ((phone-value (car (gimp-text-layer-new img "\"+91 9429806587\"," 33 PIXELS font))))
        (gimp-text-layer-set-color phone-value string-color)
        (gimp-layer-set-offsets phone-value 165 377)
        (gimp-image-insert-layer img phone-value 0 0))
      
      (let* ((email-key (car (gimp-text-layer-new img "\"email\":" 33 PIXELS font))))
        (gimp-text-layer-set-color email-key key-color)
        (gimp-layer-set-offsets email-key 189 424)
        (gimp-image-insert-layer img email-key 0 0))
      (let* ((email-value (car (gimp-text-layer-new img "\"keval.chauhan@email.com\"," 33 PIXELS font))))
        (gimp-text-layer-set-color email-value string-color)
        (gimp-layer-set-offsets email-value 165 471)
        (gimp-image-insert-layer img email-value 0 0))
      
      (let* ((website-key (car (gimp-text-layer-new img "\"website\":" 33 PIXELS font))))
        (gimp-text-layer-set-color website-key key-color)
        (gimp-layer-set-offsets website-key 189 518)
        (gimp-image-insert-layer img website-key 0 0))
      (let* ((website-value (car (gimp-text-layer-new img "\"keval.live\"" 33 PIXELS font))))
        (gimp-text-layer-set-color website-value string-color)
        (gimp-layer-set-offsets website-value 384 518)
        (gimp-image-insert-layer img website-value 0 0))
      
      (let* ((contact-close (car (gimp-text-layer-new img "}," 33 PIXELS font))))
        (gimp-text-layer-set-color contact-close text-color)
        (gimp-layer-set-offsets contact-close 165 565)
        (gimp-image-insert-layer img contact-close 0 0))
      
      (let* ((main-close (car (gimp-text-layer-new img "}" 33 PIXELS font))))
        (gimp-text-layer-set-color main-close text-color)
        (gimp-layer-set-offsets main-close 142 847)
        (gimp-image-insert-layer img main-close 0 0))
      
      ; Terminal commands
      (let* ((cmd1 (car (gimp-text-layer-new img "keval@dev:~$ npm run build" 29 PIXELS font))))
        (gimp-text-layer-set-color cmd1 '(88 214 141))
        (gimp-layer-set-offsets cmd1 47 165)
        (gimp-image-insert-layer img cmd1 0 0))
      
      (let* ((success1 (car (gimp-text-layer-new img "✓ Build successful!" 29 PIXELS font))))
        (gimp-text-layer-set-color success1 '(133 193 233))
        (gimp-layer-set-offsets success1 47 206)
        (gimp-image-insert-layer img success1 0 0))
      
      (let* ((qr-text (car (gimp-text-layer-new img "Scan QR for portfolio: keval.live" 26 PIXELS font))))
        (gimp-text-layer-set-color qr-text '(243 156 18))
        (gimp-layer-set-offsets qr-text 47 955)
        (gimp-image-insert-layer img qr-text 0 0))
      
      ; Display the image
      (gimp-display-new img)
      
      ; Return the image
      img
    )
  )
)

; Register the script for GIMP 3.0
(script-fu-register
  "script-fu-create-ide-business-card-v8"
  "IDE Business Card Template v8 (GIMP 3.0)"
  "Forces fallback font 'Sans' to avoid font issues"
  "Assistant"
  "GPL"
  "2025"
  ""
)

(script-fu-menu-register "script-fu-create-ide-business-card-v8" "<Image>/Filters/Generic")
