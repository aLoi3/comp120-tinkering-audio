import pygame
import random


class Play:
    max_channels = 5
    max_sounds = 4
    channel = [0, 0, 0, 0, 0]
    town = ['Sounds/door_close.wav',
            'Sounds/gravel_running.wav',
            'Sounds/door_close.wav',
            'Sounds/out_of_time.wav']
    cave = ['Sounds/water_drip.wav',
            'Sounds/wind_howl.wav',
            'Sounds/footsteps_cave.wav',
            'Sounds/bat_flap.wav']
    forest = ['Sounds/lake_bird_chipping.wav',
              'Sounds/door_close.wav',
              'Sounds/door_close.wav',
              'Sounds/out_of_time.wav']

    def __init__(self, location):
        self.set_channels()

    def play_base(self, location):
        """Selects the background sound for the current location"""
        base = pygame.mixer.Sound('Sounds/' + location + '.wav')
        self.channel[0].play(base)

    def set_channels(self):
        """Creates channels for the given max channels"""
        pygame.mixer.set_num_channels(self.max_channels)
        for i in range(0, self.max_channels):
            self.channel[i] = pygame.mixer.Channel(i)

    def sound_select(self, location):
        """selects a random sound from the array of sounds dependant on location"""
        random_number = random.randint(0,self.max_sounds - 1)
        selected_sound = pygame.mixer.Sound(location[random_number])
        return selected_sound

    def play_sound(self, location, channel_number):
        """Plays currently selected sound on the requested channel (never use channel 0)"""
        current_sound = self.sound_select(location)
        self.channel[channel_number].play(current_sound)

    def track_create(self, location):
        self.play_base(location)
        for i in range(0, 10):
            channel = random.randint(1, 5)
            self.play_sound(location, channel)
            pygame.time.wait(5000)



