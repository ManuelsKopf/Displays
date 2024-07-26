from PIL import Image
import numpy as np

# Bild laden
image = Image.open('Base pictures\Image1.jpeg')
image = image.convert('RGB')  # Sicherstellen, dass das Bild im RGB-Format ist

# Bild in ein NumPy-Array umwandeln
np_image = np.array(image)

# Rauschen erzeugen
noise = np.random.normal(0, 25, np_image.shape)  # Mittelwert 0, Standardabweichung 25

# Rauschen hinzufügen
np_image_noisy = np_image + noise

# Werte auf den Bereich [0, 255] beschränken
np_image_noisy = np.clip(np_image_noisy, 0, 255).astype(np.uint8)

# NumPy-Array zurück in ein Bild umwandeln
image_noisy = Image.fromarray(np_image_noisy)

# Ergebnis speichern
image_noisy.save('dein_bild_mit_rauschen.jpg')

# Optional: Ergebnis anzeigen
image_noisy.show()
