
; GIMP Script-Fu for Business Card Template
; Square format: 85mm x 85mm at 300 DPI

(define (create-business-card-template)
  (let* (
    ; Convert mm to pixels at 300 DPI: 85mm = 1003 pixels
    (img-width 1003)
    (img-height 1003)
    (img (car (gimp-image-new img-width img-height RGB)))
    (front-layer (car (gimp-layer-new img img-width img-height RGB-IMAGE "Card Front" 100 NORMAL-MODE)))
    (back-layer (car (gimp-layer-new img img-width img-height RGB-IMAGE "Card Back" 100 NORMAL-MODE)))
    (margin 60) ; 5mm margin in pixels
    )
    
    ; Add layers to image
    (gimp-image-add-layer img front-layer 0)
    (gimp-image-add-layer img back-layer 1)
    
    ; Set resolution for print
    (gimp-image-set-resolution img 300 300)
    
    ; Create front card background
    (gimp-context-set-foreground '(26 26 46)) ; Dark blue background
    (gimp-drawable-fill front-layer FOREGROUND-FILL)
    
    ; Create back card background  
    (gimp-context-set-foreground '(26 26 46)) ; Dark blue background
    (gimp-drawable-fill back-layer FOREGROUND-FILL)
    
    ; Add text layers for front card
    (let* ((name-text (car (gimp-text-fontname img -1 100 100 "KEVAL CHAUHAN" 0 TRUE 36 PIXELS "Arial Bold"))))
      (gimp-text-layer-set-color name-text '(255 255 255))
      (gimp-image-add-layer img name-text 0))
    
    (let* ((title-text (car (gimp-text-fontname img -1 100 150 "Web Developer" 0 TRUE 20 PIXELS "Arial"))))
      (gimp-text-layer-set-color title-text '(233 69 96))
      (gimp-image-add-layer img title-text 0))
    
    ; Add contact information text
    (let* ((phone-text (car (gimp-text-fontname img -1 150 220 "📞 +91 9429806587" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color phone-text '(255 255 255))
      (gimp-image-add-layer img phone-text 0))
    
    (let* ((email-text (car (gimp-text-fontname img -1 150 250 "✉ keval.chauhan@email.com" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color email-text '(255 255 255))
      (gimp-image-add-layer img email-text 0))
    
    (let* ((website-text (car (gimp-text-fontname img -1 150 280 "🌐 keval.live" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color website-text '(255 255 255))
      (gimp-image-add-layer img website-text 0))
    
    (let* ((linkedin-text (car (gimp-text-fontname img -1 150 310 "💼 linkedin.com/in/keval-s-chauhan" 0 TRUE 14 PIXELS "Arial"))))
      (gimp-text-layer-set-color linkedin-text '(255 255 255))
      (gimp-image-add-layer img linkedin-text 0))
    
    (let* ((github-text (car (gimp-text-fontname img -1 150 340 "💻 github.com/soul059" 0 TRUE 14 PIXELS "Arial"))))
      (gimp-text-layer-set-color github-text '(255 255 255))
      (gimp-image-add-layer img github-text 0))
    
    ; Add skills text
    (let* ((skills-text (car (gimp-text-fontname img -1 150 400 "Skills: HTML • CSS • JavaScript • React • Node.js • MongoDB" 0 TRUE 12 PIXELS "Arial"))))
      (gimp-text-layer-set-color skills-text '(255 255 255))
      (gimp-image-add-layer img skills-text 0))
    
    ; Add text for back card
    (gimp-image-set-active-layer img back-layer)
    
    (let* ((back-name-text (car (gimp-text-fontname img -1 300 100 "KEVAL CHAUHAN" 0 TRUE 32 PIXELS "Arial Bold"))))
      (gimp-text-layer-set-color back-name-text '(255 255 255))
      (gimp-image-add-layer img back-name-text 0))
    
    (let* ((qr-label-text (car (gimp-text-fontname img -1 350 800 "Scan for Digital Card" 0 TRUE 18 PIXELS "Arial"))))
      (gimp-text-layer-set-color qr-label-text '(255 255 255))
      (gimp-image-add-layer img qr-label-text 0))
    
    (let* ((url-text (car (gimp-text-fontname img -1 420 830 "keval.live" 0 TRUE 16 PIXELS "Arial"))))
      (gimp-text-layer-set-color url-text '(233 69 96))
      (gimp-image-add-layer img url-text 0))
    
    ; Display the image
    (gimp-display-new img)
    
    ; Return the image
    img
  )
)

; Register the script
(script-fu-register
  "create-business-card-template"
  "Business Card Template"
  "Creates a square business card template (85mm x 85mm) for Keval Chauhan"
  "Assistant"
  "GPL"
  "2025"
  ""
)

(script-fu-menu-register "create-business-card-template" "<Image>/Filters/Generic")
