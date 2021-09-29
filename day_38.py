# Day 38: Tic-Tac-Toe Pt3

import pygame, sys
import numpy as np

# Colors
BLACK = (0, 0, 0)
BLUE = (28, 170, 156)
BONE = (252, 255, 215)
LIGHT_GREEN = (175, 255, 147)
BOARD_ROWS = 3
BOARD_COLS = 3
RADIUS = 60
C_WIDTH = 15
X_WIDTH = 25
SPACE = 55

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


def draw_figures():
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS):
            if board_spaces[row][col] == 1:
                pygame.draw.circle(window, BONE, (int(col * 200 + 100), int(row * 200 + 100)), RADIUS, C_WIDTH)
            elif board_spaces[row][col] == 2:
                pygame.draw.line(window, LIGHT_GREEN, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), X_WIDTH)
                pygame.draw.line(window, LIGHT_GREEN, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), X_WIDTH)



def mark_space(row: int, col: int, p: int):
    board_spaces[row][col] = p


def is_available(row: int, col: int) -> bool:
    return board_spaces[row][col] == 0


def is_full() -> bool:
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board_spaces[row][col] == 0:
                return False
    return True


board()
player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if is_available(clicked_row, clicked_col):
                if player == 1:
                    mark_space(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_space(clicked_row, clicked_col, 2)
                    player = 1

                draw_figures()

    pygame.display.update()
