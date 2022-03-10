# Day 65: Flappy Bird Pt. 3

import pygame, os
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False

# Load images
bg = pygame.image.load('./images/Flappy/bg.png')
ground = pygame.image.load('./images/Flappy/ground.png')


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'./images/Flappy/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.click = False

    def update(self):
        # Gravity
        if flying:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if not game_over:
            # Jump
            if pygame.mouse.get_pressed()[0] == 1 and not self.click:
                self.click = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 1:
                self.click = False
                self.vel = -10

            # handle animation
            self.counter += 1
            flappy_cooldown = 5

            if self.counter > flappy_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            # Rotate bird
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)


bird_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)

run = True

while run:

    clock.tick(fps)

    # Draw background
    screen.blit(bg, (0,0))

    # Draw bird
    bird_group.draw(screen)
    bird_group.update()

    # Draw ground
    screen.blit(ground, (ground_scroll, 768))

    # Check if bird has hit the ground
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    # Draw and scroll the ground
    if not game_over:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

    pygame.display.update()

pygame.quit()