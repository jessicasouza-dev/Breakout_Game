import pygame
import screen as scrn_module
#vou escrever alguns comentários temporários em portugês mesmo, só pra vcs entenderem mais fácil caso queiram explicação
#(e quando estiver quase pronto, remover)
COLOR_BLUE = (100, 100, 255)

#criando tipo tudo
X_STARTING_POINT = 350
Y_STARTING_POINT = 600
LEFT_BORDER = 0
RIGHT_BORDER = 700
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
    
    if (mouse_x - (player.width/2) < LEFT_BORDER):
        player.midleft = (0, player.centery)
    elif (mouse_x + (player.width/2) > RIGHT_BORDER):
        player.midright = (screen.get_width(), player.centery)
    else:
        player.center = (mouse_x, player.centery)
    
    pygame.draw.rect(screen, COLOR_BLUE, player)