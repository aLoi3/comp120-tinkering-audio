import pygame
import random

pygame.mixer.init()


class Play:
    max_channels = 5
    max_sounds = 4
    channel0 = pygame.mixer.Channel(0)
    channel1 = pygame.mixer.Channel(1)
    channel2 = pygame.mixer.Channel(2)
    channel3 = pygame.mixer.Channel(3)
    channel4 = pygame.mixer.Channel(4)
    # sound = False

    def __init__(self, sound):
        self.set_channels()
        self.sound = sound
        print 'play init'

    def play_base(self, location):
        """
        Selects the background sound for the current location
        """
        base = pygame.mixer.Sound('Sounds/' + location + '.wav')
        self.channel0.play(base, loops = -1)
        print 'play base'

    def set_channels(self):
        """
        Creates channels for the given max channels
        """
        pygame.mixer.set_num_channels(self.max_channels)

    def sound_select(self, location):
        """
        selects a random sound dependant on location and plays it on its own channel
        """
        random_number = random.randint(0, self.max_sounds - 1)
        if random_number == 0:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/'+location+'1.wav'))
        if random_number == 1:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sounds/'+location+'2.wav'))
        if random_number == 2:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('Sounds/'+location+'3.wav'))
        if random_number == 3:
            pygame.mixer.Channel(4).play(pygame.mixer.Sound('Sounds/'+location+'4.wav'))
        print 'sound selected'
        print 'random sound playing now'




