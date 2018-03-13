import pygame
import Constants
import Webcam
import FileOutput()

class Main:
    def __init__(self):
        # initialize important things
        pygame.init()
        self.cam = Webcam.Webcam()
        self.file = FileOutput.FileOutput()
        self.textFont = pygame.font.SysFont('monospace', 15)
        # self.current_eye_position = (int(Constants.SCREEN_SIZE[0]/2), int(Constants.SCREEN_SIZE[1]/2) )
        # set screen width/height and caption
        # must be 16:9 aspect ratio                         
        self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE)          # testing purposes only
        # self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.FULLSCREEN)        # actual size
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
        # Loop until the user clicks close button
        while not done:
            # write event handlers here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    if event.key == pygame.K_j:
                        linesToDraw = self.cam.coordinates
                        self.draw_point_array(linesToDraw)
                        print "right", linesToDraw
                    if event.key == pygame.K_p:
                        self.screen.fill((255,255,255))
                        del linesToDraw[:]
                    if event.key == pygame.K_1:
                        self.drawPoint(self.cam.get_eyes_coordinates())
                    if event.key == pygame.K_SPACE and calibration:
                        #corner positionss
                        #0  1
                        #2  3
                        self.screen.fill((255,255,255))
                        if self.cam.get_eyes_coordinates():
                            self.corners.append(self.cam.get_eyes_coordinates())
                        else:
                            done = True
                        if cornerNumber > 3:
                            calibration = False
                            cornerNumber = cornerNumber+1
            # write logic here
            if self.calibrationMode(calibration):
                self.calibrationCircles(cornerNumber)
                # print self.current_eye_position
            else:
                self.drawPoint(self.scaledPosition(self.cam.get_eyes_coordinates()))
            #TRANSLATION INFO: X AXIS IS INVERTED
            # camera feed while app is running
            self.cam.get_webcam_feed()

            # write draw code here
                #label = self.textFont.render('text', 1, (255,255,255))
                #screen.blit(label,(X, Y))
            
            
            '''
            if len(self.cam.get_eyes_coordinates()) > 0:
                if self.cam.get_eyes_coordinates()[0] < 90:
                    pygame.draw.circle(self.screen, (0,0,0), self.cam.get_eyes_coordinates(), 2, 1)
            '''
            # display what drawn this might change
            pygame.display.update()
            # run at 60fps
            self.clock.tick(5)

    def stop(self):
        #close everything
        # print self.cam.coordinates
        self.file.writeArrayToFile(self.cam.coordinates)
        self.cam.stop_webcam()
        pygame.quit()
        print self.corners
        #checking purposes
        # print self.current_eye_position
        # print self.corners
    
    def drawPoint(self, point = (int(Constants.SCREEN_SIZE[0]/2), int(Constants.SCREEN_SIZE[1]/2))):
        pygame.draw.circle(self.screen, (0,0,0), point, 2, 1)

    
    def draw_point_array(self, coords = []):
        '''
        line = []
        for x in xrange(len(coords)):
            if x == 0 or (x % 20) == 0:
                line.append(coords[x])
        '''
        for point in coords:
            if point[0] < 90:
                pygame.draw.circle(self.screen, (0,0,0), point, 2, 1)

    def calibrationMode(self, b):
            if b:
                print "Calibration Mode"
                # if self.corners:
                    # for tmp in self.corners:
                        # print tmp
                return True
            else:
                print 'Calibration Mode off'
                #corner positionss
                        #0  1
                        #2  3
                print self.corners
                eyeWidth = self.avg(self.corners[1][0], self.corners[3][0]) - self.avg(self.corners[0][0], self.corners[2][0])
                eyeHeight = self.avg(self.corners[2][1], self.corners[3][1]) - self.avg(self.corners[0][1], self.corners[1][1])
                self.scaleX = int(Constants.SCREEN_SIZE[0]/eyeWidth)
                self.scaleY = int(Constants.SCREEN_SIZE[1]/eyeHeight)
                return False

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

    def avg(first, second):
        return int((first+second)/2)

    def scaledPosition(Coordinates = ()):
        scaledPositionX = Coordinates[0] * self.scaleX
        scaledPositionY = Coordinates[1] * self.scaleY
        return (scaledPositionX, scaledPositionY)

if __name__ == '__main__':
    game = Main()
    game.start()
    game.stop()
