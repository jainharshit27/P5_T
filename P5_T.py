import pygame

pygame.init()

screen = pygame.display.set_mode((100, 300))

t_231 = str(23*1)
t_232 = str(23*2)

font = pygame.font.Font("freesansbold.ttf", 16)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    rt_231 = font.render(t_231, True, (0, 0, 0))
    rt_232 = font.render(t_232, True, (0, 0, 0))
    
    screen.blit(rt_231, (50, 50))
    screen.blit(rt_232, (50, 70))
    
    pygame.display.update()