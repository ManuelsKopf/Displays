from PIL import Image
import numpy as np
import os

input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]

base_input_dir = 'C:\\Users\\johan\\Documents\\GitHub\\Displays\\Quadratisch Praktisch Guut'

base_output_dir = 'C:\\Users\\johan\\Documents\\GitHub\\Displays\\Generated Pictures\\Noise'


def bearbeiten1(input_image_path, output_image_path):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            image = img.convert('RGB')  # In RGB konvertieren
            np_image = np.array(image)
            noise = np.random.normal(0, 25, np_image.shape)  # Rauschen hinzufügen
            np_image_noisy = np_image + noise
            np_image_noisy = np.clip(np_image_noisy, 0, 255).astype(np.uint8)  # Werte beschneiden und zu uint8 konvertieren
            image_noisy = Image.fromarray(np_image_noisy)
            image_noisy.save(output_image_path)
            print("Penis")
            print(f"Bild gespeichert: {output_image_path}")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


for folder_number in input_folders:
    input_folder = os.path.join(base_input_dir, str(folder_number))
    output_folder = os.path.join(base_output_dir, str(folder_number))
    os.makedirs(output_folder, exist_ok=True)  
    print("First step Done")
    
    for filename in os.listdir(input_folder):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
        
            bearbeiten1(input_image_path, output_image_path)
            print("Second step done")

print('Alle Bilder wurden bearbeitet.')
