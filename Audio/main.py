import time

from tracks import *
from interface import *

# sound = False
delta_time = 0
tick_time = 0
start_time = 0
sound = False

# Pygame initialisations
pygame.init()
pygame.mixer.init()

# Main loop
def update():
    running = True  # Possible environments cave, forest, town

    start_time = time.clock()
    delta_time = 0.0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pl.update('cave')
                elif event.key == pygame.K_2:
                    pl.update('forest')
                elif event.key == pygame.K_3:
                    pl.update('town')

        # Update timing
        global tick_time
        last_time = tick_time
        tick_time = time.clock()

        delta_time = tick_time - last_time

        if delta_time >= 0.1:
            delta_time = 0.1
            
        pygame.display.update()


"""
Change location variable and run program again to hear different environments currently
"""

interface = Interface()
pl = Play(sound)
update()
pygame.quit()

