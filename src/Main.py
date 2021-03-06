import pygame
import json
import Constants
import Webcam

class Main:
    def __init__(self):
        # initialize important things
        pygame.init()
        self.cam = Webcam.Webcam()
        self.textFont = pygame.font.SysFont('monospace', 15)
        # set screen width/height and caption
        # must be 16:9 aspect ratio                         
        # self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE)          # testing purposes only
        self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.FULLSCREEN)        # actual size
        pygame.display.set_caption('Eye Tracker')

        # initialize clock. used later in the loop.
        self.clock = pygame.time.Clock()

        # clear the screen before drawing
        self.screen.fill((255, 255, 255))

    def start(self):
        #Initialize important variables
        done = False
        linesToDraw = []
        cornerNumber = 0
        self.corners = []
        calibration = True
        cornerSet = False
        imageNumber = 0
        prevTime = pygame.time.get_ticks()
        self.bg = []

        # Loop until the user clicks close button
        while not done:
            # camera feed while app is running
            self.cam.get_webcam_feed()

            # write event handlers here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    if event.key == pygame.K_1:
                        self.drawPoint(self.cam.getCurrentEyePosition)
                    if event.key == pygame.K_SPACE and calibration:
                        #corner positionss
                        #0  1
                        #2  3
                        self.screen.fill((255,255,255))
                        if self.cam.getCurrentEyePosition():
                            self.corners.append(self.cam.getCurrentEyePosition())
                            cornerNumber = cornerNumber+1
                        else:
                            done = True
                            print 'No eyes detected during calibration'
                        if cornerNumber > 3:
                            calibration = False

            # write logic here
            if calibration:
                self.calibrationCircles(cornerNumber)
            else:
                # self.drawPoint(self.cam.calculateScaledPosition(self.cam.getUnscaledPosition()))
                self.cam.addToCoordinates(self.cam.calculateScaledPosition(self.cam.getUnscaledPosition()))
            now = pygame.time.get_ticks()
            if not calibration and not cornerSet:
                self.screen.fill((0,0,0))
                prevTime = pygame.time.get_ticks()
                self.cam.setEyeCorners(self.corners)
                self.cam.setScalingWidth()
                self.cam.setScalingHeight()
                cornerSet = True
                self.loadImages(Constants.IMAGES)
            # if Constant.SECONDS has passed, load next image
            elif not calibration and cornerSet:
                if (now - prevTime) >= Constants.SECONDS:
                    prevTime = pygame.time.get_ticks()
                    # print len(self.bg)
                    if imageNumber < len(self.bg):
                        self.screen.fill((128,128,128))
                        self.screen.blit(self.bg[imageNumber], (0,0))
                    else:
                        self.screen.fill((255,255,255))
                    # print self.bg
                    imageNumber = imageNumber + 1
            
            

            # write draw code here
                #label = self.textFont.render('text', 1, (255,255,255))
                #screen.blit(label,(X, Y))

            # display what drawn this might change
            pygame.display.update()
            # run at 60fps
            self.clock.tick(60)

    def stop(self):
        #close everything
        # self.file.writeArrayToFile(self.cam.coordinates)
        self.writeToFile(self.cam.getAllCoordinates())
        # print self.cam.getEyeCorners()
        # print self.cam.getAllCoordinates()
        self.cam.stop_webcam()
        pygame.quit()
    
    def drawPoint(self, point = (int(Constants.SCREEN_SIZE[0]/2), int(Constants.SCREEN_SIZE[1]/2))):
        pygame.draw.circle(self.screen, (0,0,0), point, 2, 1)

    def loadImages(self, images):
        for i in range(len(images)):
            self.bg.append(pygame.image.load(images[i]))

    def calibrationCircles(self, cornerNum):
        if cornerNum == 0:
            # print 'top-left'
            pygame.draw.circle(self.screen, (0,0,255), (10,10), 10, 0)
        elif cornerNum == 1:
            # print 'top-right'
            pygame.draw.circle(self.screen, (0,0,255), (Constants.SCREEN_SIZE[0]-10, 10), 10, 0)
        elif cornerNum == 2:
            # print 'bottom-left'
            pygame.draw.circle(self.screen, (0,0,255), (10, Constants.SCREEN_SIZE[1]-10), 10, 0)
        elif cornerNum == 3:
            # print 'bottom-right'
            pygame.draw.circle(self.screen, (0,0,255), (Constants.SCREEN_SIZE[0]-10, Constants.SCREEN_SIZE[1]-10), 10, 0)

    def writeToFile(self, array):
        with open(Constants.FILENAME, 'w') as f:
            json.dump(array, f)


if __name__ == '__main__':
    game = Main()
    game.start()
    game.stop()
