import pygame
import screen as scrn_module
import ball as ball_module

life = 1

def show_life():
    #Tem que trocar a fonte
    global life
    life_font = pygame.font.Font("assets\PressStart2P.ttf", 44)
    life_text = life_font.render(str(life), True, scrn_module.COLOR_WHITE,scrn_module.COLOR_BLACK)
    life_text_rect = life_text.get_rect()
    life_text_rect.center = (465,25)
    
    number_font = pygame.font.Font("assets\PressStart2P.ttf", 44)
    number_text = number_font.render('1', True, scrn_module.COLOR_WHITE,scrn_module.COLOR_BLACK)
    number_text_rect = number_text.get_rect()
    number_text_rect.center = (80,25)
    
    scrn_module.screen.blit(life_text, life_text_rect)
    scrn_module.screen.blit(number_text, number_text_rect)
    
def lose_life():
    global life
    if ball_module.ball.bottom >= scrn_module.bottomlimit:
        ball_module.ball_spawn()
        life +=1 
   