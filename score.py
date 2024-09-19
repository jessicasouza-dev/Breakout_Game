import pygame
import screen as scrn_module



def inicial_score():
    #Tem que trocar a fonte
    score_font = pygame.font.Font("assets\PressStart2P.ttf", 44)
    score_text = score_font.render('000', True, scrn_module.COLOR_WHITE,scrn_module.COLOR_BLACK)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (125, 100)
    
    scrn_module.screen.blit(score_text, score_text_rect)
    
#Sem funcionalidade no momento