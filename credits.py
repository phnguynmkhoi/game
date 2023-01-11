import pygame
from pygame.locals import *
pygame.init()

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

text = "Nhom 4 \nBui Quoc Huy - 22120128 \nPhan Nguyen Minh Khoi - 22120166 \nPhan " \
      "Van Hoang Nam - 22120220 \nUong Nhat Nam - 22120221 \nDo Thanh Tung - 22120408"  \
      "\nfreepik - pch.vector - upklyak - pikisuperstar - vectorpocket - vectorpouch - johnstocker" \
      "\npictograme - coolvector - FrostC - devnewton - Pixel perfect - Umeicon - macrovector_official" \
       
def credits(screen):
    # Handle background
    WIDTH, HEIGHT = screen.get_size()
    bg_img = pygame.image.load('assets/background-menus-main.png')
    bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
    screen.blit(bg_img, (0, 0))

    # Handle texts
    blit_text(screen, text, (WIDTH/6, HEIGHT/3), get_font(30))


WIDTH, HEIGHT = 1280, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

runing = True
while runing:
    credits(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()
