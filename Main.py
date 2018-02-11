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
        self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.FULLSCREEN)
        pygame.display.set_caption('Eye Tracker')

        # initialize clock. used later in the loop.
        self.clock = pygame.time.Clock()

        # clear the screen before drawing
        self.screen.fill((255, 255, 255))

    def start(self):
        # Loop until the user clicks close button
        done = False
        while not done:
            # write event handlers here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True

            # write logic here


            # camera feed while app is running
            self.cam.get_webcam_feed()

            # write draw code here
                #label = self.textFont.render('text', 1, (255,255,255))
                #screen.blit(label,(X, Y))
            # display what drawn this might change
            pygame.display.update()
            # run at 60fps
            self.clock.tick(60)

    def stop(self):
        #close everything
        self.cam.stop_webcam()
        pygame.quit()


if __name__ == '__main__':
    game = Main()
    game.start()
    game.stop()
