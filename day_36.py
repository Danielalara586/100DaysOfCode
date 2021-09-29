# Day 36: Tic-Tac-Toe Pt1

import pygame, sys

# Colors
BLACK = (0, 0, 0)
BLUE = (28, 170, 156)

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')
window.fill(BLACK)


def board():
    # Horizontal Lines
    pygame.draw.line(window, BLUE, (0, 200), (600, 200), 15)
    pygame.draw.line(window, BLUE, (0, 400), (600, 400), 15)

    # Vertical Lines
    pygame.draw.line(window, BLUE, (200, 0), (200, 600), 15)
    pygame.draw.line(window, BLUE, (400, 0), (400, 600), 15)


board()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()




