import pygame
from window import *

pygame.init()
playing = True
win = startscreen()
okos = 0

while playing:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and okonogi.collidepoint(pygame.mouse.get_pos()):
            okos = okonogicounter(okos, win)
            print(str(okos))
        playing = quitcheck(event)



