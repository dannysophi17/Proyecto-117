import os
import cv2

ruta = "C:\\Users\\danny\\OneDrive\\Documentos\\programacion\\Proyecto 117\\Images"

Images = []

for file in os.listdir(ruta):
   
    nombre, extension = os.path.splitext(file)
    if extension.lower() in ['.png', '.jpg', '.jpeg']:
        file_name = ruta + "/" + file  
        Images.append(file_name)
        print(file_name)

count = len(Images)

if count > 0:

    frame = cv2.imread(Images[0])
    height, width, channels = frame.shape
    size = (width, height)

    print(size)
    
    out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
    
    for i in range(count):
        img = cv2.imread(Images[i])
        out.write(img)
    
    out.release()
    
    print("Fin.")
