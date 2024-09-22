import pygame
import screen as scrn_module

#criando tipo tudo
X_STARTING_POINT = 350
Y_STARTING_POINT = 660
PLAYER_BASE_WIDTH = 32
PLAYER_BASE_HEIGHT = 16

player = pygame.Rect(X_STARTING_POINT, Y_STARTING_POINT, PLAYER_BASE_WIDTH, PLAYER_BASE_HEIGHT)
player.center = (X_STARTING_POINT, Y_STARTING_POINT)

player.width = PLAYER_BASE_WIDTH
screen = scrn_module.screen
mouse_x = 0

def move():
    global player
    global mouse_x
    mouse_x = pygame.mouse.get_pos()[0]

    if (mouse_x - (player.width/2) < scrn_module.leftlimit):
        player.midleft = (0, player.centery)
    elif (mouse_x + (player.width/2) > scrn_module.rightlimit):
        player.midright = (screen.get_width(), player.centery)
    else:
        player.center = (mouse_x, player.centery)
    
    pygame.draw.rect(screen, scrn_module.COLOR_BLUE, player)

def get_hit_area(ball = pygame.rect.Rect):
    if ball.centerx <= player.left + ((player.right - player.left) / 3):
        return 0
    elif ball.centerx >= player.left + (2 * ((player.right - player.left) / 3)):
        return 2
    else:
        return 1
    
def resize(new_width):
    player.w = new_width