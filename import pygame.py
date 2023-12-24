import pygame
from sys import exit
from random import randint
def display_end_score(score):
    score_surf = test_font.render(f"Score:{score}",False,(64,64,64))
    score_rect =score_surf.get_rect(center= (400,300))
    screen.blit(score_surf,score_rect)
        
def display_score():
    score = int(pygame.time.get_ticks()/1000) - start_time    
    score_surf = test_font.render(f"Score:{score}",False,(64,64,64))
    score_rect =score_surf.get_rect(center= (400,50))
    screen.blit(score_surf,score_rect)
    return score


pygame.init()
POTENCIA_SALTO = -20
mouse_pos = pygame.mouse.get_pos()
test_font =pygame.font.Font("font/Pixeltype.ttf",50)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
game_active = False
start_time = 0
sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
#Obstacles
snail_surf =pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect =snail_surf.get_rect(midbottom=(600,300))
player_surface =pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect =player_surface.get_rect(midbottom=(100,300))
obstacle_rect_list = []

#Panatalla de inicio o game over
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400,200))
start_text_surf = test_font.render("Click space to start",False,(0,0,0))
start_text_rect = start_text_surf.get_rect(midbottom=(400,350))
game_name =test_font.render("Caracol corredor",False,(111,196,169))
game_name_rect = game_name.get_rect(center=(400,80))
#Variables dentro del loop
player_gravity = 0
score = 0
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    if player_rect.bottom>=300:
                        player_gravity += POTENCIA_SALTO
            if event.type==pygame.MOUSEMOTION:
                mouse_pos=pygame.mouse.get_pos()
                print(mouse_pos)
            
        else:
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    game_active = True
                    snail_rect.left=(800)
                    start_time = int(pygame.time.get_ticks()/1000)
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surf.get_rect(midbottom=(randint(900,1100),300)))

    if game_active:
        player_rect.y +=player_gravity        
        player_gravity+= 1        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))        
        screen.blit(player_surface,player_rect)
        screen.blit(snail_surf,snail_rect)        
        score = display_score()
        snail_rect.x -= 5
        if player_rect.bottom > 300: # ha tocado el suelo
            player_rect.bottom = 300               
            player_gravity = 0 # ya no esta saltando
        """ if snail_rect.x<-100:
            snail_rect.left=800
            """
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        if score == 0:
            screen.blit(start_text_surf,start_text_rect)
        else:
            display_end_score(score)
        screen.blit(game_name,game_name_rect)
        
    pygame.display.update()
    clock.tick(60)