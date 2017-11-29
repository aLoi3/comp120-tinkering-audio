import time

from tracks import *
from interface import *

# Pygame initialisations
pygame.init()
pygame.mixer.init()

# Main loop
def update():
    cave_on = False  # set to False on what track is currently playing
    town_on = False  # set to False on what track is currently playing
    forest_on = False  # set to False on what track is currently playing
    sound_interval = 10  # amount of second between a sound being played
    tick_time = time.time()  # initialize the t0 variable (base time)
    running = True

    while running:
        last_time = time.time()  # calculate the time since some reference point (current time)
        delta_time = last_time - tick_time  # calculate the difference in base and current time
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

        # Plays sound depending on the chosen environment
        if cave_on and delta_time >= sound_interval:
            pl.sound_selection('cave')
            tick_time = last_time  # reset base time to current time
            
        if town_on and delta_time >= sound_interval:
            pl.sound_selection('town')
            tick_time = last_time  # reset base time to current time
            
        if forest_on and delta_time >= sound_interval:
            pl.sound_selection('forest')
            tick_time = last_time  # reset base time to current time
            
        pygame.display.update()


interface = Interface()
pl = Play()
update()
pygame.quit()

