import pygame

pygame.init()
pygame.mixer.init()

window_height = 300
window_width = 800
Window = (window_width, window_height)

white = (255, 255, 255)
green = (50, 200, 50)

screen = pygame.display.set_mode(Window)


def text_surface(text, font, color):
    """Renders font and returns it and the rect
    inspiration taken from https://pythonprogramming.net/displaying-text-pygame-screen/"""
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()


def choice_screen():
    large_text = pygame.font.SysFont('arial', 50)
    small_text = pygame.font.SysFont('arial', 25)
    text_surf, text_rect = text_surface("choose your environment", small_text, white)
    text_rect.center = ((window_width/2), (window_height/8))
    screen.blit(text_surf, text_rect)

    pygame.draw.rect(screen, green, (30, 100, 200, 150))
    pygame.draw.rect(screen, green, (285, 100, 200, 150))
    pygame.draw.rect(screen, green, (540, 100, 200, 150))


running = True
choice_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
