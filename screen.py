import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (252, 252, 252)
COLOR_GREEN = (35, 142, 35)
COLOR_YELLOW = (252, 252, 0)
COLOR_ORANGE = (252, 165, 0)
COLOR_RED = (252, 0, 0)
COLOR_BLUE = (50, 153, 204)

screen_size = 600, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('breakout')

background = pygame.Surface(screen.get_size())
background = background.convert()


leftlimit = 10
rightlimit = screen.get_width() - 10
toplimit = 0
bottomlimit = 720

def edges():
    #White Edge
    pygame.draw.rect(screen,COLOR_WHITE, (0, 0, leftlimit, 720), 10)
    pygame.draw.rect(screen,COLOR_WHITE, (rightlimit, 0, 720, 720), 10)
    
    #Bricks Edge Left Side
    pygame.draw.rect(screen, (COLOR_RED) , (0, 150, leftlimit, 36), 10)
    pygame.draw.rect(screen, (COLOR_ORANGE), (0, 186, leftlimit, 36), 10)
    pygame.draw.rect(screen, (COLOR_GREEN), (0, 222, leftlimit, 36), 10)
    pygame.draw.rect(screen, (COLOR_YELLOW), (0, 258, leftlimit, 36), 10)
    
    #Bricks Edge Right Side
    pygame.draw.rect(screen,(COLOR_RED) , (rightlimit, 150, 10, 36), 10)
    pygame.draw.rect(screen,(COLOR_ORANGE), (rightlimit, 186, 10, 36), 10)
    pygame.draw.rect(screen, (COLOR_GREEN) , (rightlimit, 222, 10, 36), 10)
    pygame.draw.rect(screen, (COLOR_YELLOW), (rightlimit, 258, 10, 36), 10)
    
    #Players Edge left and right side
    pygame.draw.rect(screen,COLOR_BLUE, (0, 640, 10, 36), 10)
    pygame.draw.rect(screen,COLOR_BLUE, (rightlimit, 640, 10, 36), 10)