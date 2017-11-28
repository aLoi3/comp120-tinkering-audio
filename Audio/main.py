from tracks import *
from interface import *


def update():
    running = True  # Possible environments cave, forest, town
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pl.track_create('cave')
                elif event.key == pygame.K_2:
                    pl.track_create('forest')
                elif event.key == pygame.K_3:
                    pl.track_create('town')
        pygame.display.update()

# Pygame initialisations
pygame.init()
pygame.mixer.init()

# Main loop
"""
Change location variable and run program again to hear different environments currently
"""

interface = Interface()
pl = Play()
update()
pygame.quit()

