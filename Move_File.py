import os
import shutil

from_dir = "C:/Users/heny0/Downloads"
to_dir = "C:/Users/heny0/Downloads/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extention = os.path.splitext(file_name)

    if extention == " ":
        continue
    if extention in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = "C:/Users/heny0/Downloads/project102_file.txt"
        path2 = "C:/Users/heny0/Downloads/Document_Files/Document_Files"
        path3 = "C:/Users/heny0/Downloads/Document_Files/Document_Files/project102_file.txt"

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
        else: 
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)