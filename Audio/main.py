import pygame

pygame.init()
pygame.mixer.init()

window_height = 300
window_width = 800
Window = (window_width, window_height)

white = (255, 255, 255)
green = (50, 160, 50)

screen = pygame.display.set_mode(Window)


def text_surface(text, font, color):
    """Renders font and returns it and the rect
    inspiration taken from https://pythonprogramming.net/displaying-text-pygame-screen/"""
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()


def text_place(text, size, color, center_width, center_height):
    text_surf, text_rect = text_surface(text, size, color)
    text_rect.center = (center_width, center_height)
    screen.blit(text_surf, text_rect)


def choice_screen():
    large_text = pygame.font.SysFont('arial', 50)
    small_text = pygame.font.SysFont('arial', 25)
    text_place("Choose your environment", small_text, white, window_width/2, window_height/8)

    pygame.draw.rect(screen, green, (30, 100, 200, 150))
    pygame.draw.rect(screen, green, (290, 100, 200, 150))
    pygame.draw.rect(screen, green, (550, 100, 200, 150))



running = True
choice_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
