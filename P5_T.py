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
    
    rt_231 '''Render 1st multiple using font.render() and
    pass parameters t_231 for text to render,
    True for Antialiasing and black color code for color'''

    rt_232 #Perform similar to above code for 2nd multiple and so on.
    
    '''Paste 1st multiple using function screen.blit() and pass parameters
    rt_231 for text to paste, and (50, 50) for position'''
    
    #Perform similar to above code for 2nd multiple and so on.
    
    pygame.display.update()
