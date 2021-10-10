# Day 44: Shooter Game Pt3

import pygame
import os

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
GRAVITY = 0.75

# Colors
BG = (144, 201, 120)
RED = (255, 0, 0)

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
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.is_alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Load all images
        animation_types = ["Idle", "Run", "Jump"]

        for animation in animation_types:
            # Reset temporary list of images
            temp_list = []

            # Count number of files in a folder
            num_frames = len(os.listdir(f"./images/Shooter/{self.char_type}/{animation}"))

            for i in range(num_frames):
                img = pygame.image.load(f"./images/Shooter/{self.char_type}/{animation}/{i}.png")
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.index]
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

        if self.jump and not self.in_air:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # Apply gravity
        self.vel_y += GRAVITY

        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # Check collision
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy

    def update_anim(self):
        # Update time
        ANIM_COOLDOWN = 100
        # Update image
        self.image = self.animation_list[self.action][self.index]
        # Check time
        if pygame.time.get_ticks() - self.update_time > ANIM_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.index += 1

        # Reset animation
        if self.index >= len(self.animation_list[self.action]):
            self.index = 0

    def update_action(self, new_action):
        # Validates actions
        if new_action != self.action:
            self.action = new_action
            # Update animation settings
            self.index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Soldier("player", 200, 200, 3, 5)
enemy = Soldier("enemy", 400, 200, 3, 5)

run = True
while run:
    clock.tick(fps)

    draw_bg()

    player.update_anim()
    player.draw()
    enemy.draw()

    if player.is_alive:
        # Update player actions
        if player.in_air:
            player.update_action(2) # Jumping animation
        elif left or right:
            player.update_action(1)  # Running animation
        else:
            player.update_action(0)  # Idle animation

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
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True

    pygame.display.update()

pygame.quit()
