import pygame,sys

pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.Font('./font/Audiowide-Regular.ttf',150)
user_text='asd'

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break
        # if event.type == pygame.KEYDOWN:
        #     user_text += event.unicode
    textSurface= font.render(("Goooo!"),True,(51, 204, 204))
    screen.blit(textSurface, (0,0))
    

        