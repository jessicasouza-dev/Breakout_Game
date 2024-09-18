import pygame

screen_size = 720, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('breakout')

background = pygame.Surface(screen.get_size())
background = background.convert()