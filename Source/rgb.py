import cv2
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

input_image_path = "Base pictures\Image1.jpeg"
# Laden und Konvertieren des Bildes
rgb_image = Image.open(input_image_path)
cmyk_image = rgb_image.convert('RGB')

# Speichern des konvertierten Bildes unter einem neuen Pfad
output_image_path_2 = 'Generated Pictures\converted_image_rgb.jpg'
cmyk_image.save(output_image_path_2)


