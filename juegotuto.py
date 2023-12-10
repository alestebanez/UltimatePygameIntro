import pygame
from sys import exit
pygame.init()
mouse_pos = pygame.mouse.get_pos()
test_font =pygame.font.Font("font/Pixeltype.ttf",50)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()


score_surface = test_font.render("My game",False,(64,64,64))
score_rect = score_surface.get_rect(midbottom=(400,50))

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()

ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

snail_surf =pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect =snail_surf.get_rect(midbottom=(600,300))

player_surface =pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect =player_surface.get_rect(midbottom=(100,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                print("Jump")
        if event.type == pygame.KEYUP:
            print("Key up")
        if event.type==pygame.MOUSEBUTTONDOWN:
            print("Mousedown")
        if event.type==pygame.MOUSEBUTTONUP:
            print("Mouseup")
        if event.type==pygame.MOUSEMOTION:
            print(event.pos)
            if player_rect.collidepoint(event.pos):print("Collision")
       
            
    
   
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    
    screen.blit(player_surface,player_rect)
    screen.blit(snail_surf,snail_rect)
    pygame.draw.rect(screen,"#c0e8ec",score_rect)
    pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
    screen.blit(score_surface,score_rect)
    
    snail_rect.x -= 4
    if snail_rect.x<-100:snail_rect.left=800
    
    #if(player_rect.colliderect(snail_rect)):print("Collision")
   
    
    
    #if player_rect.collidepoint((mouse_pos)):print("Collision")
    
    
    #if player_rect.collidepoint(mouse_pos):print(pygame.mouse.get_pressed())
    """keys= pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("Jump")
    
    """
    pygame.display.update()
    clock.tick(60)
    