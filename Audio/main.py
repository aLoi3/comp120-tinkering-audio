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
    cave_on = False  #
    town_on = False  #
    forest_on = False  #
    sound_interval = 10  #
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
            pl.sound_select('cave')
            tick_time = last_time  # reset base time to current time
        elif town_on and delta_time >= sound_interval:
            pl.sound_select('town')
            tick_time = last_time  # reset base time to current time
        elif forest_on and delta_time >= sound_interval:
            pl.sound_select('forest')
            tick_time = last_time  # reset base time to current time
        elif pygame.event.type == pygame.KEYDOWN:
                if pygame.event.key == pygame.K_0:
                    break
            
        pygame.display.update()


"""
Change location variable and run program again to hear different environments currently
"""

interface = Interface()
pl = Play()
update()
pygame.quit()

