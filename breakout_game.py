#coloquem os seus nomes aqui
# -
#João Pedro Telles Paes 2415310011
#2024

import pygame
import player as plyr_module
import screen as scrn_module
import ball as ball_module
import os

#traduzir depois/ corrigindo problemas por diretório caso o jogo seja aberto por pastas exteriores:
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)

screen = scrn_module.screen

pygame.init()

# rgb color value tuples


# main loop
game_loop = True

ball = ball_module.ball
ball_module.ball_spawn()

while game_loop == True:

    screen.fill(scrn_module.COLOR_BLACK)
    
    # exiting game through the window's X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()

    plyr_module.move()

    ball_module.bounce_if_needed()
    ball_module.move()
    
    pygame.display.flip()

    pygame.time.Clock().tick(60)