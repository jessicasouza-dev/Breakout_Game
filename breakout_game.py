#coloquem os seus nomes aqui
# -
#João Pedro Telles Paes 2415310011
#2024

import pygame
import player as plyr_module
import screen as scrn_module
import ball as ball_module
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
    
    #White Edge
    pygame.draw.rect(screen, (255,255,255), (0, 0, 720, 720), 10)
    
    #Bricks Edge Left Side
    pygame.draw.rect(screen,(252, 0, 0) , (0, 150, 10, 36), 10)
    pygame.draw.rect(screen,(252, 165, 0) , (0, 186, 10, 36), 10)
    pygame.draw.rect(screen, (0, 252, 0), (0, 222, 10, 36), 10)
    pygame.draw.rect(screen, (252, 252, 0), (0, 258, 10, 36), 10)
    
    #Bricks Edge Right Side
    pygame.draw.rect(screen,(252, 0, 0) , (710, 150, 10, 36), 10)
    pygame.draw.rect(screen,(252, 165, 0) , (710, 186, 10, 36), 10)
    pygame.draw.rect(screen, (0, 252, 0), (710, 222, 10, 36), 10)
    pygame.draw.rect(screen, (252, 252, 0), (710, 258, 10, 36), 10)
    
    #Players Edge left and right side
    pygame.draw.rect(screen, (100, 100, 252), (0,580 , 10, 36), 10)
    pygame.draw.rect(screen, (100, 100, 252), (710, 580, 10, 36), 10)
    
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