#nicht fertig
import cv2
from matplotlib import pyplot as plt
import numpy as np

# Bild laden
img = cv2.imread("Base pictures\Image1.jpeg", 0)  # Graustufen

# Schwarzpunkt auf 50 setzen, Weißpunkt auf 200
#alpha = 50 / 255.0
#beta = 200 / 255.0

alpha = 100 / 255.0
beta = 150 / 255.0
new_img = cv2.normalize(img, None, alpha * 255, beta * 255, cv2.NORM_MINMAX)

# Anzeige
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(img, cmap= 'gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Cut-off')
plt.imshow(new_img, cmap='gray')
plt.axis('off')

plt.show()
 # Anzeige des Bildes
#plt.imshow(img)
#plt.show()
#plt.imshow(new_img)
#plt.show()
#cv2.imshow('Original', img)
#cv2.imshow('Cut-off', new_img)
