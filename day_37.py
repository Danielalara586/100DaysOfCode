# Day 37: Tic-Tac-Toe Pt2

import pygame, sys
import numpy as np

# Colors
BLACK = (0, 0, 0)
BLUE = (28, 170, 156)
BOARD_ROWS = 3
BOARD_COLS = 3

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')
window.fill(BLACK)

# Board
board_spaces = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board_spaces)


def board():
    # Horizontal Lines
    pygame.draw.line(window, BLUE, (0, 200), (600, 200), 15)
    pygame.draw.line(window, BLUE, (0, 400), (600, 400), 15)

    # Vertical Lines
    pygame.draw.line(window, BLUE, (200, 0), (200, 600), 15)
    pygame.draw.line(window, BLUE, (400, 0), (400, 600), 15)


def mark_space(row: int, col: int, player: int):
    board_spaces[row][col] = player


def is_available(row: int, col: int) -> bool:
    return board_spaces[row][col] == 0


def is_full() -> bool:
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board_spaces[row][col] == 0:
                return False
    return True


board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
