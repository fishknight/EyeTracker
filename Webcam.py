import cv2
import Constants

class Webcam():
    def __init__(self):
        # initialize webcam video and variables
        self.capture = cv2.VideoCapture(0)
        self.eyeCascade = cv2.CascadeClassifier(Constants.CASCADE_EYES)
        self.faceCascade = cv2.CascadeClassifier(Constants.CASCADE_FACE)
        self.coordinates = []
        self.scaleX = int(Constants.SCREEN_SIZE[0]/16)
        self.scaleY = int(Constants.SCREEN_SIZE[1]/9)

    #load webcam results in background
    def get_webcam_feed(self):
        result,ogFrame = self.capture.read()
        self.frame = ogFrame.copy()
        self.frame = cv2.flip(ogFrame, 1)
        #change video color to gray for analysis
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        #get eye position
        self.checkEyes(gray)
        
        #show camera video
        # cv2.imshow('main', self.frame)
        # cv2.imshow('gray img', gray)

    def stop_webcam(self):
        #close all windows
        self.capture.release()
        cv2.destroyAllWindows()

    def checkEyes(self, gray):
        # check face and check eye position
        # draw rectangle around detected face and eyes
        face = self.faceCascade.detectMultiScale(gray, 1.1, 3)
        for (x, y, w, h) in face:
            #cv2.rectangle(self.frame, (x, y), (x + w, y + int(h*0.6)), (255, 0, 0), 2)
            roi_eye_color = self.frame[y:y + h, x:x + w]
            roi_eye = gray[y:y + h, x:x + w]
            eye = self.eyeCascade.detectMultiScale(roi_eye)
            #cv2.line(self.frame, (x+int(w*0.5), y),(x+int(w*0.5), y+h),(255,255,0),3) 
            for (ex, ey, eh, ew) in eye:
                xCoord = int(ex + (ew / 1.8))
                yCoord = int(ey + (eh / 2.1))
                position = (xCoord, yCoord)
                if yCoord < (y + int(h * 0.35)):                     
                    cv2.circle(roi_eye_color, (xCoord, yCoord), 3, (0, 0, 255), 1)
                    if xCoord < 100:
                        self.setCurrentEyePosition(position)
                        self.addToCoordinates(position)
                #cv2.circle(roi_eye_color, (ex, ey), 3, (0, 0, 255), 1)
                #self.coordinates.append((ex, ey))
    def addToCoordinates(self, c =(0,0)):
        self.coordinates.append(c)

    def getAllCoordinates(self):
        return self.coordinates

    def setCurrentEyePosition(self, position):
        self.currentEyePosition = position

    def getCurrentEyePosition(self):
        return self.currentEyePosition
        # should return eyes coordinates

    def calculateScaledPosition(self):
        return something