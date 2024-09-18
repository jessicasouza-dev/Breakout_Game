import pygame

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (252, 252, 252)
COLOR_GREEN = (0, 252, 0)
COLOR_YELLOW = (252, 252, 0)
COLOR_RED = (252, 0, 0)

# window generatiom"
#(MUDAR TAMANHO DEPOIS PRO TAMANHO APROPRIADO)
screen_size = 720, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('breakout')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(COLOR_BLACK)

# main loop
game_loop = True

while game_loop == True:
    
    # exiting game through the window's X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()