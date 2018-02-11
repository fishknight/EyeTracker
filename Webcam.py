import cv2

class Webcam():
    def __init__(self):
        # initialize webcam video
        self.capture = cv2.VideoCapture(0)
        self.eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        self.faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #load webcam results in background
    def get_webcam_feed(self):
        result, frame = self.capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # check face and check eye position
        # draw rectangle around detected face and eyes
        face = self.faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face:
            #print "Face coordinates", x, y, w, h
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_eye_color = frame[y:y + h, x:x + w]
            roi_eye = gray[y:y + h, x:x + w]
            eye = self.eyeCascade.detectMultiScale(roi_eye)
            for (ex, ey, eh, ew) in eye:
                xCoord = int((ex + ew)/2)
                yCoord = int((ey + eh)/2)
                print "Eyes Coordinates", ex, ey,ew, eh
                cv2.circle(roi_eye_color, (xCoord, yCoord), 8, (0,0,255), 2)
                cv2.rectangle(roi_eye_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
        cv2.imshow('thing', frame)


    def stop_webcam(self):
        self.capture.release()
        cv2.destroyAllWindows()
