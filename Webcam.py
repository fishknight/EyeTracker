import cv2
import numpy

class Webcam():
    def __init__(self):
        # initialize webcam video
        self.capture = cv2.VideoCapture(0)

    #load webcam results in background
    def get_webcam_feed(self):
        result, frame = self.capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('thing', gray)
