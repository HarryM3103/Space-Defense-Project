import pygame
import random

MUSIC_PATHS_MENU = ["assets/music/8-bit-adventure.mp3",
                    "assets/music/Sawtines.mp3", "assets/music/Night Shade.mp3", "assets/music/Space Raptors.mp3", "assets/music/Aurora Borealis.mp3", "assets/music/Derezzed.mp3"]

MUSIC_PATHS_GAME = ["assets/music/Shapes.mp3",
                    "assets/music/Unfound.mp3", "assets/music/Low Earth Orbit.mp3", "assets/music/Aurora Borealis.mp3", "assets/music/Liminal.mp3"]


class MusicPlayer():

    def menuMusic(self):
        song = random.choice(MUSIC_PATHS_MENU)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.25)

    def gameMusic(self):
        song = random.choice(MUSIC_PATHS_GAME)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.10)

    def gameOver(self):
        song = "assets/music/game over.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.25)
