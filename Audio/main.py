import pygame
from tracks import *

# Pygame initialisations
pygame.init()
pygame.mixer.init()

# Variables
rect_width = 200
rect_height = 150
window_height = 300
window_width = 800
Window = (window_width, window_height)

# Different colors
white = (255, 255, 255)
green = (50, 160, 50)

screen = pygame.display.set_mode(Window)


def img_transform(image_location, size):
    """
    Loads image
    Converts to 32bit
    Transforms to the size and returns the image
    """
    temp_img = pygame.image.load(image_location)
    temp_img = temp_img.convert(32)
    temp_img = pygame.transform.scale(temp_img, size)
    return temp_img

# Sets images to variables that are called with img_transform function
# for better understanding of a code
Town = img_transform("Images/town.jpg", (rect_width, rect_height))
Forest = img_transform("Images/forest.jpg", (rect_width, rect_height))
Cave = img_transform("Images/cave.jpg", (rect_width, rect_height))


def text_surface(text, font, color):
    """
    Renders font and returns it and the rect - inspiration taken from
    https://pythonprogramming.net/displaying-text-pygame-screen/
    """
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()


def text_place(text, size, color, center_width, center_height):
    """
    Replaces the given text to the center
    """
    text_surf, text_rect = text_surface(text, size, color)
    text_rect.center = (center_width, center_height)
    screen.blit(text_surf, text_rect)


def choice_screen():
    """
    Places a text on top of a screen for clarity.
    Replaces rectangles with an appropriate image - cave, forest and town.
    Places text below images, describing what environment that is.
    """
    title = pygame.font.SysFont('arial', 25)
    text_on_button = pygame.font.SysFont('arial', 35)
    text_place("Choose your environment, press the corresponding number key", title, white, window_width/2, window_height/8)

    pygame.Surface.blit(screen, Cave, (30, 100, rect_width, rect_height))
    pygame.Surface.blit(screen, Forest, (290, 100, rect_width, rect_height))
    pygame.Surface.blit(screen, Town, (550, 100, rect_width, rect_height))

    text_place("Cave", text_on_button, white, (30 + (rect_width/2)), (100 + 170))
    text_place("Forest", text_on_button, white, (290 + (rect_width / 2)), (100 + 170))
    text_place("Town", text_on_button, white, (550 + (rect_width / 2)), (100 + 170))

    text_place("1", text_on_button, white, (30 + (rect_width / 2)), (100 + 80))
    text_place("2", text_on_button, white, (290 + (rect_width / 2)), (100 + 80))
    text_place("3", text_on_button, white, (550 + (rect_width / 2)), (100 + 80))

# Main loop
"""
Change location variable and run program again to hear different environments currently
"""
running = True  # Possible environments cave, forest, town
choice_screen()
pl = Play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pl.track_create('cave')
            if event.key == pygame.K_2:
                pl.track_create('forest')
            if event.key == pygame.K_3:
                pl.track_create('town')
    pygame.display.update()
pygame.quit()

