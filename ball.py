import pygame
import screen as scrn_module
import player as plyr_module

BALL_SPAWN_XSPEED = 0
BALL_SPAWN_YSPEED = 5

ball_starting_x = 350
ball_starting_y = 400

ball_speed_x = 0
ball_speed_y = 5

ball = pygame.Rect(ball_starting_x, ball_starting_y, 16, 16)
ball.center = (ball_starting_x, ball_starting_y)

ball_current_color = (252, 252, 252)

screen = scrn_module.screen

def ball_spawn():
    global ball_speed_x
    global ball_speed_y
    ball.centerx = ball_starting_x
    ball.centery = ball_starting_y
    pygame.draw.rect(screen, ball_current_color, ball)
    ball_speed_x = BALL_SPAWN_XSPEED
    ball_speed_y = BALL_SPAWN_YSPEED

def move():
    global ball_speed_x
    global ball_speed_y
    ball.x = (ball.x + ball_speed_x)
    ball.y = (ball.y + ball_speed_y)
    pygame.draw.rect(screen, ball_current_color, ball)

# check for conditions that cause the ball to bounce, then bounce
#se tiver alguma condição nova que faz a bola quicar, adiciona ela aqui
def try_bounce():
    global ball_speed_y
    global ball_speed_x
    if (((ball.colliderect(plyr_module.player) == True) and (ball_speed_y > 0))
        or ((ball.top <= scrn_module.toplimit) and (ball_speed_y < 0))
        or ((ball.bottom >= scrn_module.bottomlimit) and (ball_speed_y > 0))):
            ball_speed_y *= -1

    if (ball.right >= scrn_module.rightlimit
        or ball.left <= scrn_module.leftlimit):
            ball_speed_x *= -1
    
    if ball.bottom >= scrn_module.bottomlimit:
          #ativar game over aqui quando game over for implementado
          None

#ball color changing to specified color under certain conditions
def new_ball_color(new_color):
    global ball_current_color
    ball_current_color = new_color

def try_angle():
    global ball_speed_x
    global ball_speed_y
    if ball.colliderect(plyr_module.player):
        if ball.centerx >= plyr_module.player.centerx:
            ball_speed_x = abs(ball_speed_y)
        else:
            ball_speed_x = abs(ball_speed_y) * -1