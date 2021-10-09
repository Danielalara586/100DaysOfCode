# Day 43: Shooter Game Pt2

import pygame

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

# Colors
BG = (144, 201, 120)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")

# Set frame rate
clock = pygame.time.Clock()
fps = 60

# Player actions
left = False
right = False


def draw_bg():
    screen.fill(BG)


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False

        img = pygame.image.load(f"./images/Shooter/{self.char_type}/Idle/0.png")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def movement(self, moving_left, moving_right):
        # Reset movement variables
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Soldier("player", 200, 200, 3, 5)
enemy = Soldier("enemy", 400, 200, 3, 5)


run = True
while run:
    clock.tick(fps)

    draw_bg()

    player.draw()
    enemy.draw()
    player.movement(left, right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False

    pygame.display.update()

pygame.quit()
