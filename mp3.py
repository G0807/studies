# tocador de mp3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('c:/Users/milto/Downloads/Iframe Juninho Afram _ Ousado Amor _Reckless Love_ [9LOG27lJZt0].mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):
    pygame.time.Clock().tick(10)

