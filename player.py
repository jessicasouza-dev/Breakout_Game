import pygame
import screen as scrn_module

#criando tipo tudo
X_STARTING_POINT = 350
Y_STARTING_POINT = 600
PLAYER_BASE_WIDTH = 36
PLAYER_BASE_HEIGHT = 16

player = pygame.Rect(X_STARTING_POINT, Y_STARTING_POINT, PLAYER_BASE_WIDTH, PLAYER_BASE_HEIGHT)
player.center = (X_STARTING_POINT, Y_STARTING_POINT)
screen = scrn_module.screen

def move():
    global player
    mouse_x = pygame.mouse.get_pos()[0]

    #quando tivermos um valor específico de onde é o limite de distância que o jogador alcança, mudar LEFT_BORDER e RIGHT_BORDER
    #por enquanto deixei as bordas da tela como limite
    
    if (mouse_x - (player.width/2) < scrn_module.leftlimit):
        player.midleft = (0, player.centery)
    elif (mouse_x + (player.width/2) > scrn_module.rightlimit):
        player.midright = (screen.get_width(), player.centery)
    else:
        player.center = (mouse_x, player.centery)
    
    pygame.draw.rect(screen, scrn_module.COLOR_BLUE, player)