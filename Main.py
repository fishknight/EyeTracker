import pygame
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
        self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE)          # testing purposes only
        #self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.FULLSCREEN)        # actual size
        pygame.display.set_caption('Eye Tracker')

        # initialize clock. used later in the loop.
        self.clock = pygame.time.Clock()

        # clear the screen before drawing
        self.screen.fill((255, 255, 255))

    def start(self):
        # Loop until the user clicks close button
        done = False
        linesToDraw = []
        while not done:
            # write event handlers here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    if event.key == pygame.K_j:
                        linesToDraw = self.cam.get_eyes_coordinates()
                        self.draw_points(linesToDraw)
                        print "right", linesToDraw
                    if event.key == pygame.K_p:
                        self.screen.fill((255,255,255))
                        del linesToDraw[:]
                    if event.key == pygame.K_1:
                        self.drawPoint(self.cam.get_eyes_coordinates())
            # write logic here
                #CONVERT COORDINATES TO 16:9 in relation to screen

            # camera feed while app is running
            self.cam.get_webcam_feed()

            # write draw code here
                #label = self.textFont.render('text', 1, (255,255,255))
                #screen.blit(label,(X, Y))
            if self.cam.get_eyes_coordinates()[0] < 90:
                pygame.draw.circle(self.screen, (0,0,0), self.cam.get_eyes_coordinates(), 2, 1)
            # display what drawn this might change
            pygame.display.update()
            # run at 60fps
            self.clock.tick(20)

    def stop(self):
        #close everything
        self.cam.stop_webcam()
        pygame.quit()

        #checking purposes
        print self.cam.get_eyes_coordinates()
    
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
                

if __name__ == '__main__':
    game = Main()
    game.start()
    game.stop()
