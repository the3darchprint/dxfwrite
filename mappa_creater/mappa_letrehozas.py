import os

file_path = 'C:\\Projects\\Coding\\python\\dxfwrite\\mappa_creater\\mappak.txt'

base_directory = os.getcwd()

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        folder_name = line.strip() 
        if folder_name:  
            folder_path = os.path.join(base_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)  


