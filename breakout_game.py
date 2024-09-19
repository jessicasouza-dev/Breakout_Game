#coloquem os seus nomes aqui
#Isabela Braga Dutra Buleje 
#João Pedro Telles Paes 2415310011
#2024

import pygame
import player as plyr_module
import screen as scrn_module
import ball as ball_module
import score as score_module
import lifes as lifes_module
import os

#fix directory pathing issue if needed
#se em algum momento for necessário usar um asset salvo como arquivo, e o diretório
#principal não for a pasta "breakout_game", podem ocorrer problemas, isso conserta
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)

screen = scrn_module.screen

pygame.init()

# main loop
game_loop = True

ball = ball_module.ball
ball_module.ball_spawn()

while game_loop == True:

    screen.fill(scrn_module.COLOR_BLACK)
    
    scrn_module.edges()
    
    

    score_module.show_score()
    lifes_module.lose_life()
    lifes_module.show_life()
    
    # exiting game through the window's X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()

    plyr_module.move()

    ball_module.try_bounce()
    ball_module.try_angle()
    ball_module.move()
    
    pygame.display.flip()

    pygame.time.Clock().tick(60)