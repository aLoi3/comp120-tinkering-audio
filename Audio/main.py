import pygame

pygame.init()
pygame.mixer.init()

Window = (800, 300)

pygame.display.set_mode(Window)


def text_surface(text, font, color):
    """Renders font and returns it and the rect of the font
    inspiration taken from https://pythonprogramming.net/displaying-text-pygame-screen/"""
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()


def choice_screen():
    large_text = pygame.font.SysFont('arial', 110)
    small_text = pygame.font.SysFont('arial', 65)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
