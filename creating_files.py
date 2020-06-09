import os
import pickle
import cv2
from PIL import Image 
import numpy as np
import pathlib
directory = pathlib.Path(__file__).parent.absolute()
img_dir = f"{directory}/Images/"
rec = cv2.face.LBPHFaceRecognizer_create()

ide =0
lab_ids = {}

face = cv2.CascadeClassifier(f'{directory}/haarcascade_frontalface_alt2.xml') #Please paste the full path of haar cascade file

x_train = []
y_train = []

for root,dirs,files in os.walk(img_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root,file)
            label = os.path.basename(root).replace(" ","-").lower()
            
            if not label in lab_ids:
                lab_ids[label] = ide
                ide += 1

            id_ = lab_ids[label]  

            img = Image.open(path).convert("L") #converts to gray scale
            img_array = np.array(img,"uint8")
            
            faces = face.detectMultiScale(img_array,scaleFactor = 1.5, minNeighbors = 5)

            for (x,y,w,h) in faces:
                region = img_array[y:y+h, x:x+w]
                x_train.append(region)
                y_train.append(id_)     

with open(f'{directory}/label.pickle', 'wb') as f:
    pickle.dump(lab_ids, f)

rec.train(x_train, np.array(y_train))
rec.save(f"{directory}/trained.yml")
print("successfully created file")

