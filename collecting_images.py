import cv2
import pickle
import os
import time
import pathlib
directory = pathlib.Path(__file__).parent.absolute()
face = cv2.CascadeClassifier(f'{directory}/haarcascade_frontalface_alt2.xml')

img_dir = "Images/"
name = input('enter you name:          ')
label = name

font = cv2.FONT_HERSHEY_PLAIN
video = cv2.VideoCapture(0)

if os.path.isdir(f'{directory}/Images/{label}'):
    print("already exists")
else:
    os.mkdir(f'{directory}/Images/{label}') 
    a = 1
    while(True):
        if a <= 20:
            ret,frame = video.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face.detectMultiScale(gray,scaleFactor = 1.5,minNeighbors = 5)

            for (x,y,w,h) in (faces):
                if (x,y,w,h) != (0,0,0,0) and a <= 20:
                    cv2.imwrite(f'{directory}/Images/{label}/{a}.jpg',frame)
                    cv2.imshow('face',frame)
                    a += 1
                    time.sleep(0.5)
                else:
                    break 
        else:
            time.sleep(1)
            break

    print("done")

    
# Display the resulting frame
    

    