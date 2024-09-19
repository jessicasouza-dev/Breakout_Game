import pygame
import screen as scrn_module

piscando = True 
tempo_ultimo_blink = 0  
intervalo_blink = 500
score = '000'

def show_score():
    global piscando, tempo_ultimo_blink, score 
    
    tempo_atual = pygame.time.get_ticks() 
    if tempo_atual - tempo_ultimo_blink > intervalo_blink:
        piscando = not piscando 
        tempo_ultimo_blink = tempo_atual 

    if piscando:
    #Tem que trocar a fonte
        score_font = pygame.font.Font("assets\PressStart2P.ttf", 44)
        score_text = score_font.render(str(score), True, scrn_module.COLOR_WHITE,scrn_module.COLOR_BLACK)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (125, 100)
    
        scrn_module.screen.blit(score_text, score_text_rect)
        
    second_number_font = pygame.font.Font("assets\PressStart2P.ttf", 44)
    second_number_text = second_number_font.render('000', True, scrn_module.COLOR_WHITE,scrn_module.COLOR_BLACK)
    second_number_text_rect = second_number_text.get_rect()
    second_number_text_rect.center = (510, 100)
    
    scrn_module.screen.blit(second_number_text, second_number_text_rect)
    
#Sem funcionalidade no momento