import Constants
import cv2


class Webcam:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        if self.capture.isOpened():  # Checks the stream
            self.frameSize = (int(self.capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)),
                              int(self.capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)))
        Constants.SCREEN_HEIGHT = self.frameSize[0]
        Constants.SCREEN_WIDTH = self.frameSize[1]
