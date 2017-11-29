import pygame
import random

pygame.mixer.init()


class Play:
    """
    Sets channels, chooses sound randomnly depending on
    the chosen environment and plays it.

    Attributes:
        max_channels (int): maximum amount of channels
        max_sounds (int): maximum amount of sounds played
        channel (pygame.mixer.Channel): five channels for sounds 
    """
    
    max_channels = 5
    max_sounds = 4
    channel0 = pygame.mixer.Channel(0)
    channel1 = pygame.mixer.Channel(1)
    channel2 = pygame.mixer.Channel(2)
    channel3 = pygame.mixer.Channel(3)
    channel4 = pygame.mixer.Channel(4)

    def __init__(self):
        self.channel_selection()

    def play_base(self, location):
        """
        Selects the background sound for the current location
        """
        
        base = pygame.mixer.Sound('Sounds/' + location + '.wav')
        self.channel0.play(base, loops=-1)

    def channel_selection(self):
        """
        Creates channels for the given max channels
        """
        
        pygame.mixer.set_num_channels(self.max_channels)

    def sound_selection(self, location):
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
            




