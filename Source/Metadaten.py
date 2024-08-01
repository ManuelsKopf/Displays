import os
import csv

def get_image_paths_and_folders(base_input_dir, input_folders):
    image_info_list = []

    for folder_number in input_folders:
        input_folder = os.path.join(base_input_dir, str(folder_number))
        
        # Überprüfen, ob der Ordner existiert
        if not os.path.exists(input_folder):
            print(f"Ordner {input_folder} existiert nicht.")
            continue
        
        for filename in os.listdir(input_folder):
            input_image_path = os.path.join(input_folder, filename)
            
            if os.path.isfile(input_image_path):  # Überprüfen, ob es sich um eine Datei handelt
                image_info = {
                    "path": input_image_path,
                    "folder": folder_number
                }
                image_info_list.append(image_info)

    return image_info_list

def save_to_csv(image_info_list, output_csv_path):
    # Spaltennamen für die CSV-Datei
    fieldnames = ['path', 'folder']
    
    # Schreiben der Daten in die CSV-Datei
    with open(output_csv_path, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()  # Schreiben der Spaltennamen
        for info in image_info_list:
            writer.writerow(info)


# Beispiel für die Verwendung
base_input_dir = 'Generated Pictures 2\Pixeldichte'
input_folders = [1, 2, 4, 7, 11, 12, 13, 14, 15, 17, 18, 21, 22, 23, 26, 27, 32, 33, 35, 38]
output_csv_path = 'CSV\Pixeldichte.csv'


image_info_list = get_image_paths_and_folders(base_input_dir, input_folders)
save_to_csv(image_info_list, output_csv_path)

open(output_csv_path)

