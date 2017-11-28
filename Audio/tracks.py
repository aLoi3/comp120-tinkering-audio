import pygame
import random


class Play:
    max_channels = 10
    max_sounds = 10
    channel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    town = []
    cave = []
    forest = []

    def __init__(self, location):
        self.set_channels()

    def play_base(self, location):
        """Selects the background sound for the current location"""
        base = pygame.mixer.Sound('Sounds/', location, '.wav')
        self.channel[0].play(base)

    def set_channels(self):
        """Creates channels for the given max channels"""
        pygame.mixer.set_num_channels(self.max_channels)
        for i in range(0, self.max_channels - 1):
            self.channel[i] = pygame.mixer.Channel(i)

    def sound_select(self, location):
        """selects a random sound from the array of sounds dependant on location"""
        random_number = random.randint(1,self.max_sounds - 1)
        selected_sound = pygame.mixer.Sound(location[random_number])
        return selected_sound

    def play_sound(self, location, channel_number):
        """Plays currently selected sound on the requested channel"""
        current_sound = self.sound_select(location)
        self.channel[channel_number].play(current_sound)







#channel1.play(good_sound)
#channel2.play(bad_sound)
#channel3.play(crow)