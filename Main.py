import pygame
import Constants


class Main():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        pygame.display.set_caption("CustomEyeTracker")