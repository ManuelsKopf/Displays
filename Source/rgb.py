#nicht fertig
import cv2
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import os


input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]

base_input_dir = 'C:/Users/johan/VSC-Projects/Displays/Quadratisch Praktisch Guut'

base_output_dir = 'C:/Users/johan/VSC-Projects/Displays/Generated Pictures'  


def bearbeiten(input_image_path, output_image_path):
    with Image.open(input_image_path) as img:   
        img = img.convert('RGB')
        pixels = img.load()

        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (255 - r, 255 - g, 255 - b)
    
            img.save(output_image_path)

for folder_number in input_folders:
    input_folder = os.path.join(base_input_dir, str(folder_number))
    output_folder = os.path.join(base_output_dir, str(folder_number))
    os.makedirs(output_folder, exist_ok=True)  

    # Alle Dateien im Eingabeordner durchlaufen
    for filename in os.listdir(input_folder):
        if filename.startswith(('IMG')):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            
            # Bild bearbeiten und speichern
            bearbeiten(input_image_path, output_image_path)


print('Alle Bilder wurden bearbeitet.')