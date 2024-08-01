#nicht fertig
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from PIL import Image, ImageEnhance

input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]

base_input_dir = 'Reduced pictures'

base_output_dir = 'Generated Pictures\HistogramCut'

def save_image_with_suffix(img, output_folder, base_filename, suffix):
    output_image_path = os.path.join(output_folder, f"{base_filename}_{suffix}.png")
    img.save(output_image_path)
    print(f"Bild gespeichert: {output_image_path}")


def bearbeiten3(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            image = img.convert('RGB') 
            np_image = np.array(image)
            alpha = 100 / 255.0
            beta = 150 / 255.0
            new_img = cv2.normalize(np_image, None, alpha * 255, beta * 255, cv2.NORM_MINMAX)
            new_image = Image.fromarray(new_img)
            save_image_with_suffix(new_image, output_folder, base_filename, 'histogram_cut')
            print("Penis")
            print(f"Bild gespeichert: {output_folder}")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")



for folder_number in input_folders:
    input_folder = os.path.join(base_input_dir, str(folder_number))
    output_folder = os.path.join(base_output_dir, str(folder_number))
    os.makedirs(output_folder, exist_ok=True)  
    print("First step Done")
    
    for filename in os.listdir(input_folder):
            input_image_path = os.path.join(input_folder, filename)
            
            if os.path.isfile(input_image_path):
                base_filename, ext = os.path.splitext(filename)
                bearbeiten3(input_image_path,output_folder,base_filename)


print('Alle Bilder wurden bearbeitet.')







# Anzeige
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.title('Original')
# plt.imshow(img, cmap= 'gray')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.title('Cut-off')
# plt.imshow(new_img, cmap='gray')
# plt.axis('off')

# plt.show()
 # Anzeige des Bildes
#plt.imshow(img)
#plt.show()
#plt.imshow(new_img)
#plt.show()
#cv2.imshow('Original', img)
#cv2.imshow('Cut-off', new_img)
