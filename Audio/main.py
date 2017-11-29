import time
from tracks import *
from interface import *


def update():
    cave_on = False
    town_on = False
    forest_on = False
    sound_interval = 10
    t0 = time.time()  # initialize the t0 variable (base time)
    running = True
    while running:
        t1 = time.time()  # calculate the time since some reference point (current time)
        dt = t1 - t0  # calculate the difference in base and current time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pl.play_base('cave')
                    cave_on = True
                    town_on = False
                    forest_on = False
                if event.key == pygame.K_2:
                    pl.play_base('forest')
                    cave_on = False
                    town_on = False
                    forest_on = True
                if event.key == pygame.K_3:

                    pl.play_base('town')
                    cave_on = False
                    town_on = True
                    forest_on = False
        if cave_on and dt >= sound_interval:
            pl.sound_select('cave')
            t0 = t1  # reset base time to current time
        if town_on and dt >= sound_interval:
            pl.sound_select('town')
            t0 = t1  # reset base time to current time
        if forest_on and dt >= sound_interval:
            pl.sound_select('forest')
            t0 = t1  # reset base time to current time
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

