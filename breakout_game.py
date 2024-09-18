#coloquem os seus nomes aqui
# -
#João Pedro Telles Paes 2415310011
#2024

import pygame
import player_functions as plyr_module
import screen as scrn_module
import os

#traduzir depois/ corrigindo problemas por diretório caso o jogo seja aberto por pastas exteriores:
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)



screen = scrn_module.screen

pygame.init()

# rgb color value tuples
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (252, 252, 252)
COLOR_GREEN = (0, 252, 0)
COLOR_YELLOW = (252, 252, 0)
COLOR_ORANGE = (252, 165, 0)
COLOR_RED = (252, 0, 0)
COLOR_BLUE = (100, 100, 252)

# main loop
game_loop = True

while game_loop == True:

    screen.fill(COLOR_BLACK)
    
    # exiting game through the window's X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()

    plyr_module.move()
    
    pygame.display.flip()

    pygame.time.Clock().tick(60)