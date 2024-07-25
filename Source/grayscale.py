import cv2
import numpy as np
import matplotlib.pyplot as plt

# Bildpfad
image_path = "Base pictures\Image1.jpeg"

# Bild laden und in Graustufen konvertieren
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Funktion zur Anpassung der Helligkeit
def increase_brightness(image, value):
    # Clip the values to stay within valid range [0, 255]
    brightness_image = np.clip(image + value, 0, 255).astype(np.uint8)
    return brightness_image

# Anzahl der Schritte und der Helligkeitswert pro Schritt
num_steps = 10
brightness_step = 20

# Erhöhung der Graustufen in Schritten
for step in range(num_steps):
    increased_gray = increase_brightness(gray, step * brightness_step)
    
    # Anzeige des Bildes
    plt.imshow(increased_gray, cmap='gray')
    plt.title(f'Step {step + 1}: Brightness {step * brightness_step}')
    plt.show()

    # Speichern des Bildes (optional)
    cv2.imwrite(f'Generated Pictures\Gray-Scale-{step + 1}.jpg', increased_gray)

