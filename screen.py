import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (252, 252, 252)
COLOR_GREEN = (0, 252, 0)
COLOR_YELLOW = (252, 252, 0)
COLOR_ORANGE = (252, 165, 0)
COLOR_RED = (252, 0, 0)
COLOR_BLUE = (100, 100, 252)

screen_size = 720, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('breakout')

background = pygame.Surface(screen.get_size())
background = background.convert()

leftlimit = 0
rightlimit = 720
toplimit = 0
bottomlimit = 720