import os
import shutil

# path = "Downloads"
# path2 = "C:/Users/Juinior/Desktop/Maria/PYTHON/Aula 102/assets/background.png"
# doc, extension = os.path.splitext(path2)

# print(doc)
# print(extension)

source = "C:/Users/Juinior/Desktop/Maria/PYTHON/Aula 102/assets"
destination = "C:/Users/Juinior/Desktop/Maria/PYTHON/Aula 102/assets2"

# if os.path.exists(destination):
#     print("Pasta já criada.")
# else:
#     os.mkdir(destination)
#     print("A pasta foi criada.")
    
list_of_files = os.listdir(source)

for file in list_of_files:
    name, extension = os.path.splitext(file)

    if extension == "":
        continue
    if extension in [".png", ".jpg", ".gif", ".jpeg", ".jfif"]:
        path_1 = source+"/"+file
        path_2 = destination+"/"+"images" 
        path_3 = path_2+"/"+file

        if os.path.exists(path_2):
            print(f"Movendo {file}...")
            shutil.move(path_1, path_3)
        else:
            os.mkdir(path_2)
            print(f"Movendo {file}...")
            shutil.move(path_1, path_3)

    if extension in [".mp3", ".wav"]:
        path_1 = source+"/"+file
        path_2 = destination+"/"+"audios" 
        path_3 = path_2+"/"+file

        if os.path.exists(path_2):
            print(f"Movendo {file}...")
            shutil.move(path_1, path_3)
        else:
            os.mkdir(path_2)
            print(f"Movendo {file}...")
            shutil.move(path_1, path_3)
