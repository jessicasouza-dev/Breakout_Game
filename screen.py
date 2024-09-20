import pygame

import tiles

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

def edges():
    #White Edge
    pygame.draw.rect(screen,COLOR_WHITE, (0, 0, 10, 720), 10)
    pygame.draw.rect(screen,COLOR_WHITE, (710, 0, 720, 720), 10)
    
    #Bricks Edge Left Side
    pygame.draw.rect(screen, (COLOR_RED) , (0, 150, 10, 36), 10)
    pygame.draw.rect(screen, (COLOR_ORANGE), (0, 186, 10, 36), 10)
    pygame.draw.rect(screen, (COLOR_GREEN), (0, 222, 10, 36), 10)
    pygame.draw.rect(screen, (COLOR_YELLOW), (0, 258, 10, 36), 10)
    
    #Bricks Edge Right Side
    pygame.draw.rect(screen,(COLOR_RED) , (710, 150, 10, 36), 10)
    pygame.draw.rect(screen,(COLOR_ORANGE), (710, 186, 10, 36), 10)
    pygame.draw.rect(screen, (COLOR_GREEN) , (710, 222, 10, 36), 10)
    pygame.draw.rect(screen, (COLOR_YELLOW), (710, 258, 10, 36), 10)
    
    #Players Edge left and right side
    pygame.draw.rect(screen,COLOR_BLUE, (0,580 , 10, 36), 10)
    pygame.draw.rect(screen,COLOR_BLUE, (710, 580, 10, 36), 10)