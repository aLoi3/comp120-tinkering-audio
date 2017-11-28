import pygame
import random


class Play:
    max_channels = 10
    max_sounds = 10
    channel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    town = []
    cave = []
    forest = []

    def __init__(self):
        self.set_channels()

    def play_base(self, location):
        base = pygame.mixer.Sound('Sounds/', location, '.wav')
        self.channel[0].play(base)

    def set_channels(self):
        pygame.mixer.set_num_channels(self.max_channels)
        for i in range(0, self.max_channels - 1):
            self.channel[i] = pygame.mixer.Channel(i)

    def sound_select(self, location):
        random_number = random.randint(1,self.max_sounds - 1)
        selected_sound = location[random_number]
        return selected_sound




#channel1.play(good_sound)
#channel2.play(bad_sound)
#channel3.play(crow)