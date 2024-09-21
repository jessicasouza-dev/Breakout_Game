#Isabela Braga Dutra Buleje 
#João Pedro Telles Paes 2415310011
#Jessica Rodrigues de Souza
#2024

import pygame
import player as plyr_module
import screen as scrn_module
import ball as ball_module
import score as score_module
import lifes as lifes_module
import os
import tiles

ROWS = 8
COLS = 14

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

wall = tiles.Wall(ROWS, COLS, screen, scrn_module.leftlimit, 155)

isRound = False

while game_loop == True:

    screen.fill(scrn_module.COLOR_BLACK)
    scrn_module.edges()
    wall.draw()
    score_module.show_score()
    lifes_module.lose_life(wall)
    lifes_module.show_life()

    # exiting game through the window's X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()
        if event.type == pygame.KEYDOWN and isRound == False:
            isRound = True
            lifes_module.life = 3
            score_module.score = 0
            wall.redraw()
            ball_module.ball_respawn()

    if lifes_module.life > 0 and isRound:
        plyr_module.player.width = plyr_module.PLAYER_BASE_WIDTH
        plyr_module.move()

        ball_module.try_bounce(isRound)
        ball_module.collide_brick(wall, isRound)
        ball_module.move()
        ball_module.new_ball_color()
        
        pygame.display.flip()

        pygame.time.Clock().tick(60)

    elif isRound == False or lifes_module.life <= 0:
        isRound = False
        plyr_module.player.width = scrn_module.screen_size[0]
        plyr_module.move()

        ball_module.try_bounce(isRound)
        ball_module.collide_brick(wall, isRound)
        ball_module.move()
        
        pygame.display.flip()

        pygame.time.Clock().tick(60)
