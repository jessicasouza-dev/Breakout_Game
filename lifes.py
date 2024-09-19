import pygame
import screen as scrn_module
import ball as ball_module

def inicial_life():
    #Tem que trocar a fonte
    life = 1
    life_font = pygame.font.Font("assets\PressStart2P.ttf", 44)
    life_text = life_font.render("1", True, scrn_module.COLOR_WHITE,scrn_module.COLOR_BLACK)
    life_text_rect = life_text.get_rect()
    life_text_rect.center = (465,25)
    
#Depois adiciono a perda de vida, agora apenas é visual
   