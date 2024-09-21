import pygame
import screen as scrn_module
import player as plyr_module
import score as scr_module
import random

BALL_SPAWN_XSPEED = 0
BALL_SPAWN_YSPEED = 5

ball_starting_x = random.randint(120,400)
ball_starting_y = 400

ball_speed_x = 0
ball_speed_y = 5

ROWS = 8
COLS = 14

ball = pygame.Rect(ball_starting_x, ball_starting_y, 8, 8)
ball.center = (ball_starting_x, ball_starting_y)

ball_current_color = (252, 252, 252)

pygame.mixer.init()
ball_hitting_block = pygame.mixer.Sound('assets/Ball hit Block.wav')
ball_hitting_paddle = pygame.mixer.Sound('assets/Ball hit Paddle.wav')
ball_hitting_wall = pygame.mixer.Sound('assets/Ball hit Wall.wav')

screen = scrn_module.screen

isActive = True
ball_angle = 0


def ball_spawn():
    global ball_speed_x
    global ball_speed_y
    global ball_starting_x
    global ball_starting_y
    ball_starting_x = random.randint(100,600)
    ball.centerx = ball_starting_x
    ball.centery = ball_starting_y
    pygame.draw.rect(screen, ball_current_color, ball)
    if ball_starting_x < 360:
        ball_speed_x = 1
    if ball_starting_x > 360:
        ball_speed_x = -1
    ball_speed_y = BALL_SPAWN_YSPEED
    



def ball_respawn():
    ball.centerx = 0
    ball.centery = 0
    pygame.draw.rect(screen, ball_current_color, pygame.Rect(0, 0, 0, 0))
    '''ball_speed_x = 0
    ball_speed_y = 0'''

    ball_spawn()


# main funtion to move the ball every frame
def move():
    global ball_speed_x
    global ball_speed_y

    # actual movement
    ball.x = (ball.x + ball_speed_x)
    ball.y = (ball.y + ball_speed_y)
    pygame.draw.rect(screen, ball_current_color, ball)


# check for conditions that cause the ball to bounce, then bounce
def try_bounce():
    global ball_speed_y
    global ball_speed_x
    global isActive
    global ball_angle
    #ball collides with player or top of screen
    if ((ball.top <= scrn_module.toplimit) and (ball_speed_y < 0)):
        ball_speed_y *= -1
        isActive = True
        ball_hitting_wall.play()
    #ball collides with left of screen
    if (ball.right >= scrn_module.rightlimit
            or ball.left <= scrn_module.leftlimit):
        ball_speed_x *= -1
        ball_hitting_wall.play()

    #ball trajectory change if it does collide with player
    if ((ball.colliderect(plyr_module.player) == True)
            and (ball_speed_y > 0)):
        ball_speed_y *= -1
        isActive = True
        ball_hitting_paddle.play()
        if plyr_module.get_hit_area(ball) == 0:
            ball_angle = 0
        if plyr_module.get_hit_area(ball) == 1:
            if ball_speed_x < 0:
                ball_angle = 1
            else:
                ball_angle = 2
        if plyr_module.get_hit_area(ball) == 2:
            ball_angle = 3

        angle_calibrate()


def angle_calibrate():
    global ball_speed_x
    global ball_speed_y
    global ball_angle

    if ball_angle == 0:
        ball_speed_x = abs(ball_speed_y) * -1
    elif ball_angle == 1:
        ball_speed_x = (abs(ball_speed_y) * (2 / 3)) * -1
    elif ball_angle == 2:
        ball_speed_x = (abs(ball_speed_y) * (2 / 3))
    elif ball_angle == 3:
        ball_speed_x = abs(ball_speed_y)


#ball color changing to specified color under certain conditions
def new_ball_color():
    global ball_current_color
    if 294 > ball.y >= 258:
        ball_current_color = scrn_module.COLOR_YELLOW
    elif 258 > ball.y >= 222:
        ball_current_color = scrn_module.COLOR_GREEN
    elif 222 > ball.y >= 186:
        ball_current_color = scrn_module.COLOR_ORANGE
    elif 186 > ball.y >= 150:
        ball_current_color = scrn_module.COLOR_RED
    elif 640 > ball.y >= 628:
        ball_current_color = scrn_module.COLOR_BLUE
    else:
        ball_current_color = (252, 252, 252)  # Cor padrão (branco)
    pygame.draw.rect(screen, ball_current_color, ball)



def collide_brick(wall, isRound):
    global ball_speed_x
    global ball_speed_y
    global isActive
    for row in wall.tiles:
        for brick in row:
            if ball.colliderect(brick.rect):
                if isActive == True:
                    ball_hitting_block.play()
                    isActive = False
                    ball_speed_y *= -1

                    brick.bounces -= 1

                    if brick.bounces < 1 and isRound:
                        brick.rect = pygame.Rect(0, 0, 0, 0)
                        row.remove(brick)

                        if len(row) < 1:
                            print(f"COLUNA {brick.color} ACABOU")

                        scr_module.score += brick.points

                        if brick.color not in wall.colors and isRound:
                            wall.colors.append(brick.color)
                            ball_speed_y += brick.speed
                            print(wall.colors)
                            angle_calibrate()
