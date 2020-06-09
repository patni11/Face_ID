from playsound import playsound
import sys
import pathlib
import os
directory = pathlib.Path(__file__).parent.absolute()
import pickle #To save and retrieve weights
from Face_Recogniser import Face_Detector
import cv2
import pyautogui


face = Face_Detector()
font = cv2.FONT_HERSHEY_PLAIN
rec = cv2.face.LBPHFaceRecognizer_create() #rec for trec or recognizer
print(directory)
rec.read(f'{directory}/trained.yml') #Use the full path of your trained.yml file. This file contains the weights for your face


vid = cv2.VideoCapture(0)

while (vid.isOpened()):
    _,frame = vid.read()
    frame = cv2.flip(frame,1)
    img,roi,x,y = face.detect(frame)

    with open(f'{directory}/label.pickle','rb') as f: #Use the full path of your lable.pickle file. This file contains the name of recognized users
        labels = {a:b for b,a in pickle.load(f).items()}
    if roi != "No Face Detected":
        idd,conf = rec.predict(roi)
        
        if conf >= 0.8: 
            if labels[idd] == "shubh":   #Enter the name as in label.pickle file, for which the computer should log in 
                pyautogui.click()             
                pyautogui.write('Windows_Sucks')   #Enter you password here
                pyautogui.press('enter')
                os.system("test")
                os.system("say welcome shubh")   #Ask it to say whatever you want when user logs in
                break
            else:
                os.system("test")
                os.system("say eat shit")  #Ask it to say whatever you want when someone else logs in
        else:
            os.system("test")
            os.system("say eat shit")    #Ask it to say whatever you want when someone else logs in        
            #cv2.putText(img,labels[idd],(x,y + 20),font,1,(0,255,0),2)  

    #cv2.imshow('img',img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()
playsound(f'{directory}/napalm_death.mp3') #Replace this with the music of your choice. Or comment it if you do not want music