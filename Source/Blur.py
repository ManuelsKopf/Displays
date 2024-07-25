import cv2
import matplotlib.pyplot as plt
#passt
# Bildpfad
image_path_blur = "Base pictures\Image1.jpeg"

# Bild laden
img_blur = cv2.imread(image_path_blur)
img_rgb_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB)

# Gaussian Blur anwenden --> Glätten von scharfen Kanten --> schnitt von allen Pixel
gaussian_blur = cv2.GaussianBlur(img_rgb_blur, (15, 15), 0)

# Box Blur anwenden 
# Dies geschieht durch Faltung eines Bildes mit einem normalisierten Boxfilter. Es wird einfach der Durchschnitt aller 
# Pixel unter dem Kernelbereich genommen und das zentrale Element ersetzt. 
box_blur = cv2.blur(img_rgb_blur, (15, 15))

# Median Blur anwenden --> verändert die Sachen hinter dem Kernel
median_blur = cv2.medianBlur(img_rgb_blur, 15)

# Bilder anzeigen
plt.figure(figsize=(15, 10))

plt.subplot(1, 4, 1)
plt.title('Originalbild')
plt.imshow(img_rgb_blur)

plt.subplot(1, 4, 2)
plt.title('Gaussian Blur')
plt.imshow(gaussian_blur)

plt.subplot(1, 4, 3)
plt.title('Box Blur')
plt.imshow(box_blur)

plt.subplot(1, 4, 4)
plt.title('Median Blur')
plt.imshow(median_blur)

plt.show()

# Ergebnisse speichern (optional)
cv2.imwrite('Generated Pictures/gaussian_blur.jpg', cv2.cvtColor(gaussian_blur, cv2.COLOR_RGB2BGR))
cv2.imwrite('Generated Pictures/box_blur.jpg', cv2.cvtColor(box_blur, cv2.COLOR_RGB2BGR))
cv2.imwrite('Generated Pictures/median_blur.jpg', cv2.cvtColor(median_blur, cv2.COLOR_RGB2BGR))


# Zweite Stufe
# Gaussian Blur anwenden --> Glätten von scharfen Kanten --> schnitt von allen Pixel
gaussian_blur_2 = cv2.GaussianBlur(img_rgb_blur, (51, 51), 0)

# Box Blur anwenden 
# Dies geschieht durch Faltung eines Bildes mit einem normalisierten Boxfilter. Es wird einfach der Durchschnitt aller 
# Pixel unter dem Kernelbereich genommen und das zentrale Element ersetzt. 
box_blur_2 = cv2.blur(img_rgb_blur, (51, 51))

# Median Blur anwenden --> verändert die Sachen hinter dem Kernel
median_blur_2 = cv2.medianBlur(img_rgb_blur, 51)

# Bilder anzeigen
plt.figure(figsize=(15, 10))

plt.subplot(1, 4, 1)
plt.title('Originalbild')
plt.imshow(img_rgb_blur)

plt.subplot(1, 4, 2)
plt.title('Gaussian Blur')
plt.imshow(gaussian_blur_2)

plt.subplot(1, 4, 3)
plt.title('Box Blur')
plt.imshow(box_blur_2)

plt.subplot(1, 4, 4)
plt.title('Median Blur')
plt.imshow(median_blur_2)

plt.show()

# Ergebnisse speichern (optional)
cv2.imwrite('Generated Pictures/gaussian_blur.jpg', cv2.cvtColor(gaussian_blur_2, cv2.COLOR_RGB2BGR))
cv2.imwrite('Generated Pictures/box_blur.jpg', cv2.cvtColor(box_blur_2, cv2.COLOR_RGB2BGR))
cv2.imwrite('Generated Pictures/median_blur.jpg', cv2.cvtColor(median_blur_2, cv2.COLOR_RGB2BGR))




# Dritte Stufe
# Gaussian Blur anwenden --> Glätten von scharfen Kanten --> schnitt von allen Pixel
gaussian_blur_3 = cv2.GaussianBlur(img_rgb_blur, (101, 101), 0)

# Box Blur anwenden
# Dies geschieht durch Faltung eines Bildes mit einem normalisierten Boxfilter. Es wird einfach der Durchschnitt aller
# Pixel unter dem Kernelbereich genommen und das zentrale Element ersetzt.
box_blur_3 = cv2.blur(img_rgb_blur, (101, 101))

# Median Blur anwenden --> verändert die Sachen hinter dem Kernel
median_blur_3 = cv2.medianBlur(img_rgb_blur, 101)

# Bilder anzeigen
plt.figure(figsize=(15, 10))

plt.subplot(1, 4, 1)
plt.title('Originalbild')
plt.imshow(img_rgb_blur)

plt.subplot(1, 4, 2)
plt.title('Gaussian Blur')
plt.imshow(gaussian_blur_3)

plt.subplot(1, 4, 3)
plt.title('Box Blur')
plt.imshow(box_blur_3)

plt.subplot(1, 4, 4)
plt.title('Median Blur')
plt.imshow(median_blur_3)

plt.show()

# Ergebnisse speichern (optional)
cv2.imwrite('Generated Pictures/gaussian_blur.jpg', cv2.cvtColor(gaussian_blur_3, cv2.COLOR_RGB2BGR))
cv2.imwrite('Generated Pictures/box_blur.jpg', cv2.cvtColor(box_blur_3, cv2.COLOR_RGB2BGR))
cv2.imwrite('Generated Pictures/median_blur.jpg', cv2.cvtColor(median_blur_3, cv2.COLOR_RGB2BGR))


