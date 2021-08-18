import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

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
    screen.blit(background, (50, 50))
    screen.blit(omok_black, (50, 50))
    screen.blit(omok_white, (100, 100))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        print("mouse left click")
        print(event.button)
        print(pygame.mouse.get_pos()) 

    pygame.display.update()
    clock.tick(30) # fps
pygame.quit()
    
