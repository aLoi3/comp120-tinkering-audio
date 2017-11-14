import pygame
import numpy
import math


pygame.mixer.init()
pygame.init()

Window = (800, 600)

pygame.display.set_mode(Window)


Frequency = 2000
Frequency_l = 2000
Frequency_r = 3000
Bits = 16
Sample_rate = 44100
Duration = 1.0
Volume = 100

value = []

n_samples = int(round(Duration * Sample_rate))

buf = numpy.zeros((n_samples, 2), dtype=numpy.int16)
max_sample = 2**(Bits - 1) - 1

for i in range(n_samples):
    t = float(i) / Sample_rate

    buf[i][0] = math.sin(2.0 * math.pi * Frequency_l * t) * (Volume * Bits)
    buf[i][1] = math.sin(2.0 * math.pi * Frequency_r * t) * (Volume * Bits)

sound = pygame.sndarray.make_sound(buf)
sound.play(loops=-1)


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break

pygame.quit()
