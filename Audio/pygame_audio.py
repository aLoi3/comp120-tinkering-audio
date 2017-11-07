import pygame
import numpy

def change_volume(samples, volume_change):
    for sample in samples:
        sample *= volume_change  # doubles sound


pygame.init()
pygame.mixer.init()

pygame.display.set_mode((800,600))

#pygame.mixer.music.load('bensound-littleidea.mp3')
#pygame.mixer.music.play()  # To do, make music start and stop on key press

bad_sound = pygame.mixer.Sound("chewbacca_01.wav")
bad_sample = pygame.sndarray.samples(bad_sound)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bad_sound.play()
            if event.key == pygame.K_UP:
                change_volume(bad_sample, 2)
            if event.key == pygame.K_DOWN:
                change_volume(bad_sound, 0.5)
    pygame.display.update()
pygame.quit()


