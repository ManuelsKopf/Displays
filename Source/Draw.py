import cv2
import numpy as np
import matplotlib.pyplot as plt
# Pfad zum Bild angeben
image_path = "Quadratisch Praktisch Guut\1\IMG_1201.PNG"

# Bild laden
image = cv2.imread(image_path)

# Funktion zum Zeichnen der Figur
def draw_figure(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK :
        global drawing, top_left, bottom_right
        if event == cv2.EVENT_LBUTTONDBLCLK :
            drawing = True
            top_left = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            bottom_right = (x, y)
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# Fenster erstellen und Funktion für Mausklicks festlegen
#cv2.namedWindow("Bild")
cv2.setMouseCallback("Bild", draw_figure)

# Bild anzeigen
plt.imshow(image)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()