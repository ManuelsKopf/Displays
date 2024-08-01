from PIL import Image
import numpy as np
import os

input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]

base_input_dir = 'Reduced pictures'

base_output_dir = 'Generated Pictures/Noise'


def save_image_with_suffix(img, output_folder, base_filename, suffix):
    output_image_path = os.path.join(output_folder, f"{base_filename}_{suffix}.png")
    img.save(output_image_path)
    print(f"Bild gespeichert: {output_image_path}")

def generatePicture(input_image_path, output_image_path, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            image = img.convert('RGB')  
            np_image = np.array(image)
            noise = np.random.normal(0, 25, np_image.shape) 
            np_image_noisy = np.clip(np_image_noisy, 0, 255).astype(np.uint8) 
            image_noisy = Image.fromarray(np_image_noisy)
            save_image_with_suffix(image_noisy, output_folder, base_filename, 'Noise')
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
            if os.path.isfile(input_image_path):
                base_filename, ext = os.path.splitext(filename)
                generatePicture(input_image_path, output_image_path, base_filename)
                print("Second step done")

