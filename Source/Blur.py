import cv2
import matplotlib.pyplot as plt
from PIL import Image 
import os
import numpy as np


input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]

base_input_dir = 'C:\\Users\\johan\\Documents\\GitHub\\Displays\\Quadratisch Praktisch Guut'

base_output_dir = 'C:\\Users\\johan\\Documents\\GitHub\\Displays\\Generated Pictures\\Noise\\Blur'

def save_image_with_suffix(img, output_folder, base_filename, suffix):
    output_image_path = os.path.join(output_folder, f"{base_filename}_{suffix}.png")
    img.save(output_image_path)
    print(f"Bild gespeichert: {output_image_path}")


def bearbeiten4(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            img_rgb_blur = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
            img_rgb_blur_pil = Image.fromarray(img_rgb_blur)
            save_image_with_suffix(img_rgb_blur_pil, output_folder, base_filename, "edit1")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")

def bearbeiten5(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            box_blur = cv2.blur(np_image, (15, 15))
            box_blur_pil = Image.fromarray(box_blur)
            save_image_with_suffix(box_blur_pil, output_folder, base_filename, "edit2")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def bearbeiten6(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            median_blur = cv2.medianBlur(np_image, 15)
            median_blur_pil = Image.fromarray(median_blur)
            save_image_with_suffix(median_blur_pil, output_folder, base_filename, "edit3")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def bearbeiten7(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            gaussian_blur_2 = cv2.GaussianBlur(np_image, (51, 51), 0)
            gaussian_blur_2_pil = Image.fromarray(gaussian_blur_2)
            save_image_with_suffix(gaussian_blur_2_pil, output_folder, base_filename, "edit4")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def bearbeiten8(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            box_blur_2 = cv2.blur(np_image, (51, 51))
            box_blur_2_pil = Image.fromarray(box_blur_2)
            save_image_with_suffix(box_blur_2_pil, output_folder, base_filename, "edit5")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")

def bearbeiten9(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            median_blur_2 = cv2.medianBlur(np_image, 51)
            median_blur_2_pil = Image.fromarray(median_blur_2)
            save_image_with_suffix(median_blur_2_pil, output_folder, base_filename, "edit6")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def bearbeiten10(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            gaussian_blur_3 = cv2.GaussianBlur(np_image, (101, 101), 0)
            gaussian_blur_3_pil = Image.fromarray(gaussian_blur_3)
            save_image_with_suffix(gaussian_blur_3_pil, output_folder, base_filename, "edit7")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def bearbeiten11(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            box_blur_3 = cv2.blur(np_image, (101, 101))
            box_blur_3_pil = Image.fromarray(box_blur_3)
            save_image_with_suffix(box_blur_3_pil, output_folder, base_filename, "edit8")
            print("Third Step Done")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def bearbeiten12(input_image_path, output_folder, base_filename):
    print(f"Bearbeite Bild: {input_image_path}")
    try:
        with Image.open(input_image_path) as img:
            np_image = np.array(img)
            median_blur_3 = cv2.medianBlur(np_image, 101)
            median_blur_3_pil = Image.fromarray(median_blur_3)
            save_image_with_suffix(median_blur_3_pil, output_folder, base_filename, "edit9")
            print("Third Step Done")
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

                bearbeiten4(input_image_path, output_folder, base_filename)
                bearbeiten5(input_image_path, output_folder, base_filename)
                bearbeiten6(input_image_path, output_folder, base_filename)
                bearbeiten7(input_image_path, output_folder, base_filename)
                bearbeiten8(input_image_path, output_folder, base_filename)
                bearbeiten9(input_image_path, output_folder, base_filename)
                bearbeiten10(input_image_path, output_folder, base_filename)
                bearbeiten11(input_image_path, output_folder, base_filename)
                bearbeiten12(input_image_path, output_folder, base_filename)



                print("Second step done")

print('Alle Bilder wurden bearbeitet.')



















# image_path_blur = "Base pictures\Image1.jpeg"

# # Bild laden
# img_blur = cv2.imread(image_path_blur)
# img_rgb_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB)

# # Gaussian Blur anwenden --> Glätten von scharfen Kanten --> schnitt von allen Pixel
# gaussian_blur = cv2.GaussianBlur(img_rgb_blur, (15, 15), 0)

# # Box Blur anwenden 
# # Dies geschieht durch Faltung eines Bildes mit einem normalisierten Boxfilter. Es wird einfach der Durchschnitt aller 
# # Pixel unter dem Kernelbereich genommen und das zentrale Element ersetzt. 
# box_blur = cv2.blur(img_rgb_blur, (15, 15))

# # Median Blur anwenden --> verändert die Sachen hinter dem Kernel
# median_blur = cv2.medianBlur(img_rgb_blur, 15)




# # Zweite Stufe
# # Gaussian Blur anwenden --> Glätten von scharfen Kanten --> schnitt von allen Pixel
# gaussian_blur_2 = cv2.GaussianBlur(img_rgb_blur, (51, 51), 0)

# # Box Blur anwenden 
# # Dies geschieht durch Faltung eines Bildes mit einem normalisierten Boxfilter. Es wird einfach der Durchschnitt aller 
# # Pixel unter dem Kernelbereich genommen und das zentrale Element ersetzt. 
# box_blur_2 = cv2.blur(img_rgb_blur, (51, 51))

# # Median Blur anwenden --> verändert die Sachen hinter dem Kernel
# median_blur_2 = cv2.medianBlur(img_rgb_blur, 51)







# # Dritte Stufe
# # Gaussian Blur anwenden --> Glätten von scharfen Kanten --> schnitt von allen Pixel
# gaussian_blur_3 = cv2.GaussianBlur(img_rgb_blur, (101, 101), 0)

# # Box Blur anwenden
# # Dies geschieht durch Faltung eines Bildes mit einem normalisierten Boxfilter. Es wird einfach der Durchschnitt aller
# # Pixel unter dem Kernelbereich genommen und das zentrale Element ersetzt.
# box_blur_3 = cv2.blur(img_rgb_blur, (101, 101))

# # Median Blur anwenden --> verändert die Sachen hinter dem Kernel
# median_blur_3 = cv2.medianBlur(img_rgb_blur, 101)





# # Bilder anzeigen
# plt.figure(figsize=(15, 10))

# plt.subplot(1, 4, 1)
# plt.title('Originalbild')
# plt.imshow(img_rgb_blur)

# plt.subplot(1, 4, 2)
# plt.title('Gaussian Blur')
# plt.imshow(gaussian_blur)

# plt.subplot(1, 4, 3)
# plt.title('Box Blur')
# plt.imshow(box_blur)

# plt.subplot(1, 4, 4)
# plt.title('Median Blur')
# plt.imshow(median_blur)

# plt.show()

# # Ergebnisse speichern (optional)
# cv2.imwrite('Generated Pictures/gaussian_blur.jpg', cv2.cvtColor(gaussian_blur_3, cv2.COLOR_RGB2BGR))
# cv2.imwrite('Generated Pictures/box_blur.jpg', cv2.cvtColor(box_blur_3, cv2.COLOR_RGB2BGR))
# cv2.imwrite('Generated Pictures/median_blur.jpg', cv2.cvtColor(median_blur_3, cv2.COLOR_RGB2BGR))




# # Bilder anzeigen
# plt.figure(figsize=(15, 10))

# plt.subplot(1, 4, 1)
# plt.title('Originalbild')
# plt.imshow(img_rgb_blur)

# plt.subplot(1, 4, 2)
# plt.title('Gaussian Blur')
# plt.imshow(gaussian_blur_2)

# plt.subplot(1, 4, 3)
# plt.title('Box Blur')
# plt.imshow(box_blur_2)

# plt.subplot(1, 4, 4)
# plt.title('Median Blur')
# plt.imshow(median_blur_2)

# plt.show()

# # Ergebnisse speichern (optional)
# cv2.imwrite('Generated Pictures/gaussian_blur.jpg', cv2.cvtColor(gaussian_blur_2, cv2.COLOR_RGB2BGR))
# cv2.imwrite('Generated Pictures/box_blur.jpg', cv2.cvtColor(box_blur_2, cv2.COLOR_RGB2BGR))
# cv2.imwrite('Generated Pictures/median_blur.jpg', cv2.cvtColor(median_blur_2, cv2.COLOR_RGB2BGR))





# # Bilder anzeigen
# plt.figure(figsize=(15, 10))

# plt.subplot(1, 4, 1)
# plt.title('Originalbild')
# plt.imshow(img_rgb_blur)

# plt.subplot(1, 4, 2)
# plt.title('Gaussian Blur')
# plt.imshow(gaussian_blur_3)

# plt.subplot(1, 4, 3)
# plt.title('Box Blur')
# plt.imshow(box_blur_3)

# plt.subplot(1, 4, 4)
# plt.title('Median Blur')
# plt.imshow(median_blur_3)


# # Ergebnisse speichern (optional)
# cv2.imwrite('Generated Pictures/gaussian_blur.jpg', cv2.cvtColor(gaussian_blur, cv2.COLOR_RGB2BGR))
# cv2.imwrite('Generated Pictures/box_blur.jpg', cv2.cvtColor(box_blur, cv2.COLOR_RGB2BGR))
# cv2.imwrite('Generated Pictures/median_blur.jpg', cv2.cvtColor(median_blur, cv2.COLOR_RGB2BGR))