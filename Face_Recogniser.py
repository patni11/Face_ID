import cv2
import os
import pathlib
directory = pathlib.Path(__file__).parent.absolute()

class Face_Detector():
        
    def detect(self,video,boxes=False):
        frame = video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = cv2.CascadeClassifier(f'{directory}/haarcascade_frontalface_default.xml')
        faces = face.detectMultiScale(gray,scaleFactor = 1.5,minNeighbors = 5)
        
        if faces != ():
            for (x,y,w,h) in faces:
                roi = gray[y:y+h, x:x+h]   
                roi_main = roi    
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                if boxes:
                    x2 = int(x+(5*w/2)+10)
                    y2 = int((3*y/2)+h)
                    cv2.rectangle(frame,(x+w+10,y),(x2,y2),(0,255,0),4)    
                    ROI = [(x+w+10,y),(x2,y2)]
                else:
                    X = x
                    Y = y
                    ROI = roi_main    
        else:
            if boxes:
                height,width,*_ = frame.shape
                cv2.rectangle(frame,(int(0.65*width),0),(width,int(height//1.5)),(0,0,255),4)
                ROI = [(int(0.65*width),0),(width,int(height//1.5))]
            else:
                ROI = "No Face Detected"
                X = 'no'
                Y = 'no'
        return frame,ROI,X,Y
            


