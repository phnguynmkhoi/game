import pygame
from pygame.locals import *
import function
pygame.init()
def credit(screen,username):
    WIDTH, HEIGHT = screen.get_size()
    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def blit_text(surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    text = "Nhom 4 \nBui Quoc Huy - 22120128 \nPhan Nguyen Minh Khoi - 22120166 \nPham " \
        "Van Hoang Nam - 22120220 \nUong Nhat Nam - 22120221 \nDo Thanh Tung - 22120408"  \
        "\nfreepik - pch.vector - upklyak - pikisuperstar - vectorpocket - vectorpouch - johnstocker - starline - Creative_hat" \
        "\npictograme - coolvector - FrostC - devnewton - Pixel perfect - Umeicon - macrovector_official" \
        
    def credits(screen):
        Left = WIDTH*0.1
        Top = HEIGHT*0.8

        bg_img = pygame.image.load('banner/credit.png')
        bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
        screen.blit(bg_img, (0, 0))

        # Handle texts
        if WIDTH >=1280:
            blit_text(screen, text, (WIDTH/6, HEIGHT/4), get_font(30))
        else: 
            blit_text(screen, text, (WIDTH/6, HEIGHT/4), get_font(24))

        #nút back
        back = pygame.image.load('Image/assets/SetMenu/back.png').convert()
        back = pygame.transform.scale(back,(WIDTH*0.15,HEIGHT*0.1))
        back1 = pygame.image.load('Image/assets/Mode/back-hover.png').convert()
        back1 = pygame.transform.scale(back1,(WIDTH*0.15,HEIGHT*0.1))

        BACK_OBJECT = pygame.Rect(Left,Top,WIDTH*0.15,HEIGHT*0.1)
        BACK_LOCATION = (Left,Top)

        mouse = pygame.mouse.get_pos()
        if BACK_OBJECT.collidepoint(mouse):
            screen.blit(back1,(Left,Top))
        else:
            screen.blit(back,(Left,Top))

    #window = pygame.display.set_mode((WIDTH, HEIGHT))
    runing = True
    while runing:
        credits(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                runing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                function.main_menu(screen,username,selection_main_mennu=0)
        pygame.display.update()
    pygame.quit()