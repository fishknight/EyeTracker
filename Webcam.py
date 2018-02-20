import cv2
import Constants

class Webcam():
    def __init__(self):
        # initialize webcam video
        self.capture = cv2.VideoCapture(0)
        self.rightEyeCascade = cv2.CascadeClassifier(Constants.CASCADE_RIGHT_EYE)
        self.leftEyeCascade = cv2.CascadeClassifier(Constants.CASCADE_LEFT_EYE)
        self.faceCascade = cv2.CascadeClassifier(Constants.CASCADE_FACE)
        self.coordinates = []

    #load webcam results in background
    def get_webcam_feed(self):
        result, self.frame = self.capture.read()

        #change video color to gray for analysis
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        #get eye position
        self.get_eye_position(gray)

        #show camera video
        cv2.imshow('thing', self.frame)

    def stop_webcam(self):
        #close all windows
        self.capture.release()
        cv2.destroyAllWindows()

    def get_eye_position(self, gray):
        # check face and check eye position
        # draw rectangle around detected face and eyes
        face = self.faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face:
            #cv2.rectangle(self.frame, (x, y), (x + w, y + int(h*0.6)), (255, 0, 0), 2)
            roi_eye_color = self.frame[y:y + h, x:x + w]
            roi_eye = gray[y:y + h, x:x + w]
            right_eye = self.eyeCascade.detectMultiScale(roi_eye)
            for (ex, ey, eh, ew) in eye:
                xCoord = int(ex + (ew / 1.8))
                yCoord = int(ey + (eh / 2.1))
                if yCoord < (y + int(h*0.35)): 
                    cv2.circle(roi_eye_color, (xCoord, yCoord), 3, (0, 0, 255), 1)
                    self.coordinates.append((xCoord, yCoord))

    def get_eyes_coordinates(self):
        recordedCoordinates = []
        for x in xrange(len(self.coordinates)):
            if x == 0 or (x % 20) == 0:
                recordedCoordinates.append(self.coordinates[x])
        return recordedCoordinates
        # should return eyes coordinates
    