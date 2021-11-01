import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino_rect = pygame.Rect(100, 250, 64, 64)
cactus_rect = pygame.Rect(1100, 300, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

dino_y_change = 0

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if -----.type == pygame.-------:           #SA1
            if event.--- == pygame.-------:        #SA1
                ------------- = 1  
        #if -----.type == pygame.-------:           #SA2
        #    if event.--- == pygame.-------:        #SA2
        #        ------------- = 1                  #SA2
    
    dino_rect.y += dino_y_change
     if dino_rect.y __ 100:                        #SA1
        dino_rect.y __ 100
     #if dino_rect.y __ 250:                        #SA2
     #   dino_rect.y __ 250                         #SA2   

    cactus_rect.x = cactus_rect.x - 1
    if cactus_rect.x <= -30:
        cactus_rect.x = 1200
        
    pygame.draw.rect(screen, (100, 100, 100), dino_rect)
    pygame.draw.rect(screen, (100, 100, 100), cactus_rect)
    pygame.draw.rect(screen, (100, 100, 100), ground_rect)
    
    pygame.display.update()
    
    
    
    
    
