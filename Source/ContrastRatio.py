from PIL import Image, ImageEnhance

# Bild laden
image = Image.open('Base pictures\Image1.jpeg')

# Kontrast anpassen
enhancer = ImageEnhance.Contrast(image)
image_enhanced = enhancer.enhance(0.8)  # 0.5 verringert den Kontrast, 1.0 ist das Original, Werte > 1 erhöhen den Kontrast

# Ergebnis speichern
image_enhanced.save('Base pictures\Image1234.jpeg')

# Optional: Ergebnis anzeigen
image_enhanced.show()
