import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("ul omok")


oo = 53
spot_pos = 50/2
block = 50
running = True
nemo = -1

while running:
    if nemo == -1:
        apb = "a"
    if nemo == 0:
        apb = "b"
    if nemo == 1:
        apb = "c"
    if nemo == 2:
        apb = "d"
    if nemo == 3:
        apb = "e"
    if nemo == 4:
        apb = "f"
    if nemo == 5:
        apb = "g"
    if nemo == 6:
        apb = "h"
    if nemo == 7:
        apb = "i"
    if nemo == 8:
        apb = "j"
    if nemo == 9:
        apb = "k"
    if nemo == 10:
        apb = "l"
    if nemo == 11:
        apb = "n"
    if nemo == 12:
        apb = "m"
    if nemo == 13:
        apb = "o"
    for i in range(15):
        globals()[f"{apb}{i}"] = [oo + (i * 50), (oo + block*(nemo+1))]
    nemo += 1
    if nemo > 13:
        running = False

run = True

background = pygame.image.load("src/img/omok_board.png") # omok_board
background = pygame.transform.scale(background, (700, 700))

#load
omok_black = pygame.image.load("src/img/omok_black.png")
omok_white = pygame.image.load("src/img/omok_white.png")
#scale
omok_black = pygame.transform.scale(omok_black, (50, 50))
omok_white = pygame.transform.scale(omok_white, (50, 50))

while run:
    screen.blit(background, (53, 53))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = list(pygame.mouse.get_pos())
        print(mouse_pos)

        

    pygame.display.update()
    clock.tick(30) # fps
pygame.quit()
    
