import pygame
import Constants



class Main():
    def __init__(self):
        # initialize important things
        pygame.init()

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
                    if event.key == pygame.K_q:
                        done = True
                    if event.key == pygame.K_w:
                        self.screen.fill((0, 0, 0))
                    if event.key == pygame.K_e:
                        self.screen.fill((0, 0, 255))
                    if event.key == pygame.K_r:
                        self.screen.fill((0, 128, 255))

            # write game logic here

            # write draw code here
                #screen.blit(img,(X, Y))
            # display what drawn this might change
            pygame.display.update()
            # run at 60fps
            self.clock.tick(60)

if __name__ == '__main__':
    game = Main()
    game.start()

    # close the windows and quit
    pygame.quit()