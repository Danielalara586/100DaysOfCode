# Day 45: Shooter Game Pt4

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
shoot = False

# Load images
bullet_img = pygame.image.load('./images/Shooter/icons/bullet.png').convert_alpha()


def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.is_alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.health = 100
        self.max_health = self.health
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
        animation_types = ["Idle", "Run", "Jump", "Death"]

        for animation in animation_types:
            # Reset temporary list of images
            temp_list = []

            # Count number of files in a folder
            num_frames = len(os.listdir(f"./images/Shooter/{self.char_type}/{animation}"))

            for i in range(num_frames):
                img = pygame.image.load(f"./images/Shooter/{self.char_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.update_anim()
        self.check_alive()

        # Update cool down
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

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

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 10
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1

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
            if self.action == 3:
                self.index = len(self.animation_list[self.action]) - 1
            else:
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

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.is_alive = False
            self.update_action(3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # Move bullet
        self.rect.x += (self.direction * self.speed)

        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH - 100:
            self.kill()

        # Check collisions with characters
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 5
                self.kill()

        if pygame.sprite.spritecollide(enemy, bullet_group, False):
            if enemy.alive:
                enemy.health -= 25
                self.kill()


# Sprites group
bullet_group = pygame.sprite.Group()

player = Soldier("player", 200, 200, 3, 5, 20)
enemy = Soldier("enemy", 400, 200, 3, 5, 20)

run = True
while run:
    clock.tick(fps)

    draw_bg()

    player.update()
    player.draw()

    enemy.update()
    enemy.draw()

    # Update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)

    # Update player actions
    if player.is_alive:
        # Shoot bullets
        if shoot:
            player.shoot()
        if player.in_air:
            player.update_action(2)  # Jumping animation
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
            if event.key == pygame.K_RETURN:
                shoot = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_RETURN:
                shoot = False

    pygame.display.update()

pygame.quit()
