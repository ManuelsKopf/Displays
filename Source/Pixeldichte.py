from PIL import Image
import os



input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]

base_input_dir = 'Reduced pictures'

base_output_dir = 'Generated Pictures 2\Pixeldichte'

def save_image_with_suffix(img, output_folder, base_filename, suffix):
    output_image_path = os.path.join(output_folder, f"{base_filename}_{suffix}.png")
    img.save(output_image_path)
    print(f"Bild gespeichert: {output_image_path}")



def verschlechtere_auflösung50(input_image_path, output_folder, base_filename):
    try:
        with Image.open(input_image_path) as img:
            original_width, original_height = img.size
            new_width = int(original_width * 0.5)
            new_height = int(original_height * 0.5)
            img_resized_down = img.resize((new_width, new_height), Image.LANCZOS)
            img_resized_up = img_resized_down.resize((original_width, original_height), Image.NEAREST)
            save_image_with_suffix(img_resized_up, output_folder, base_filename, "fifty")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def verschlechtere_auflösung10(input_image_path, output_folder, base_filename):
    try:
        with Image.open(input_image_path) as img:
            original_width, original_height = img.size
            new_width = int(original_width * 0.1)
            new_height = int(original_height * 0.1)
            img_resized_down = img.resize((new_width, new_height), Image.LANCZOS)
            img_resized_up = img_resized_down.resize((original_width, original_height), Image.NEAREST)
            save_image_with_suffix(img_resized_up, output_folder, base_filename, "ten")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")


def verschlechtere_auflösung4(input_image_path, output_folder, base_filename):
    try:
        with Image.open(input_image_path) as img:
            original_width, original_height = img.size
            new_width = int(original_width * 0.04)
            new_height = int(original_height * 0.04)
            img_resized_down = img.resize((new_width, new_height), Image.LANCZOS)
            img_resized_up = img_resized_down.resize((original_width, original_height), Image.NEAREST)
            save_image_with_suffix(img_resized_up, output_folder, base_filename, "four")
    except Exception as e:
        print(f"Fehler beim Bearbeiten von {input_image_path}: {e}")



for folder_number in input_folders:
    input_folder = os.path.join(base_input_dir, str(folder_number))
    output_folder = os.path.join(base_output_dir, str(folder_number))
    os.makedirs(output_folder, exist_ok=True)  
    print("First step Done")
    
    for filename in os.listdir(input_folder,):
            base_filename, ext = os.path.splitext(filename)

            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
        
            verschlechtere_auflösung50(input_image_path, output_folder, base_filename)
            verschlechtere_auflösung10(input_image_path, output_folder, base_filename)
            verschlechtere_auflösung4(input_image_path, output_folder, base_filename)
            print("Second step done")

print('Alle Bilder wurden bearbeitet.')
