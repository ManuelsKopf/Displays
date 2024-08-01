import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]

base_input_dir = 'Reduced pictures'

base_output_dir = 'Generated Pictures\Gray Scale'


def save_image_with_suffix(img, output_folder, base_filename, suffix):
    output_image_path = os.path.join(output_folder, f"{base_filename}_{suffix}.png")
    cv2.imwrite(output_image_path, img)
    print(f"Bild gespeichert: {output_image_path}")

# Funktion zur Anpassung der Helligkeit
def increase_brightness(image, value):
    # Clip the values to stay within valid range [0, 255]
    brightness_image = np.clip(image + value, 0, 255).astype(np.uint8)
    return brightness_image

def generatePicture(input_image_path, output_folder, base_filename):
        print(f"Bearbeite Bild: {input_image_path}")
        try:
            img = cv2.imread(input_image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            num_steps = 10
            brightness_step = 20
            # Erhöhung der Graustufen in Schritten
            for step in range(num_steps):
                increased_gray = increase_brightness(gray, step * brightness_step)
                save_image_with_suffix(increased_gray, output_folder, base_filename, 'Grayscale' + str (step * brightness_step) )
                print(f"Bild gespeichert: {output_folder}")
        except Exception as e:
            print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")

# Erhöhung der Graustufen in Schritten
for folder_number in input_folders:
    input_folder = os.path.join(base_input_dir, str(folder_number))
    output_folder = os.path.join(base_output_dir, str(folder_number))
    os.makedirs(output_folder, exist_ok=True)  
    print("First step Done")
    
    for filename in os.listdir(input_folder):
            input_image_path = os.path.join(input_folder, filename)
            
            if os.path.isfile(input_image_path):
                base_filename, ext = os.path.splitext(filename)
                generatePicture(input_image_path,output_folder,base_filename)



