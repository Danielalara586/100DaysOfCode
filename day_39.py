# Day 39: Tic-Tac-Toe Pt4

import pygame, sys
import numpy as np

# Colors
BLACK = (0, 0, 0)
BLUE = (28, 170, 156)
BONE = (252, 255, 215)
LIGHT_GREEN = (175, 255, 147)

WIDTH = 600
HEIGHT = 600
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
RADIUS = SQUARE_SIZE // 3
C_WIDTH = 15
X_WIDTH = 25
SPACE = SQUARE_SIZE//4


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
window.fill(BLACK)

# Board
board_spaces = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board_spaces)


def board():
    # Horizontal Lines
    pygame.draw.line(window, BLUE, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), 15)
    pygame.draw.line(window, BLUE, (0, SQUARE_SIZE*2), (WIDTH, SQUARE_SIZE*2), 15)

    # Vertical Lines
    pygame.draw.line(window, BLUE, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), 15)
    pygame.draw.line(window, BLUE, (SQUARE_SIZE*2, 0), (SQUARE_SIZE*2, HEIGHT), 15)


def draw_figures():
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS):
            if board_spaces[row][col] == 1:
                pygame.draw.circle(window, BONE, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), RADIUS, C_WIDTH)
            elif board_spaces[row][col] == 2:
                pygame.draw.line(window, LIGHT_GREEN, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), X_WIDTH)
                pygame.draw.line(window, LIGHT_GREEN, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), X_WIDTH)


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


def check_win(p: int) -> bool:
    # Vertical win check
    for col in range(BOARD_COLS):
        if board_spaces[0][col] == p and board_spaces[1][col] == p and board_spaces[2][col] == p:
            draw_vertical_winning_line(col, p)
            return True

    # Horizontal win check
    for row in range(BOARD_ROWS):
        if board_spaces[row][0] == p and board_spaces[row][1] == p and board_spaces[row][2] == p:
            draw_horizontal_winning_line(row, p)
            return True

    # Ascending win check
    if board_spaces[2][0] == p and board_spaces[1][1] == p and board_spaces[0][2]:
        draw_asc_diagonal(p)
        return True

    # Descending win check
    if board_spaces[0][0] == p and board_spaces[1][1] == p and board_spaces[2][2] == p:
        draw_desc_diagonal(p)
        return True

    return False


def draw_vertical_winning_line(col: int, p: int):
    pos_x = col * SQUARE_SIZE + SQUARE_SIZE//2

    if p == 1:
        color = BONE
    elif p == 2:
        color = LIGHT_GREEN

    pygame.draw.line(window, color, (pos_x, 15), (pos_x, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row: int, p: int):
    pos_y = row * SQUARE_SIZE + 100

    if p == 1:
        color = BONE
    elif p == 2:
        color = LIGHT_GREEN

    pygame.draw.line(window, color, (15, pos_y), (WIDTH - 15, pos_y), 15)


def draw_asc_diagonal(p: int):
    if p == 1:
        color = BONE
    elif p == 2:
        color = LIGHT_GREEN

    pygame.draw.line(window, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(p: int):
    if p == 1:
        color = BONE
    elif p == 2:
        color = LIGHT_GREEN

    pygame.draw.line(window, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    window.fill(BLACK)
    board()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board_spaces[row][col] = 0


board()
player = 1
game_over = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if is_available(clicked_row, clicked_col):
                mark_space(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True

                player = player % 2 + 1
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
