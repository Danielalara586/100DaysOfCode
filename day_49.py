# Day 49: Shooter Game Pt8

import pygame
import os
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
GRAVITY = 0.75
TILE_SIZE = 50

# Colors
BG = (144, 201, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")

# Set frame rate
clock = pygame.time.Clock()
fps = 60

# Player actions
left = False
right = False
shoot = False
grenade = False
is_thrown = False

# Load images
bullet_img = pygame.image.load('./images/Shooter/icons/bullet.png').convert_alpha()
grenade_img = pygame.image.load('./images/Shooter/icons/grenade.png').convert_alpha()

# Pick up boxes
health_box_img = pygame.image.load("./images/Shooter/icons/health_box.png").convert_alpha()
ammo_box_img = pygame.image.load("./images/Shooter/icons/ammo_box.png").convert_alpha()
grenade_box_img = pygame.image.load("./images/Shooter/icons/grenade_box.png").convert_alpha()
item_box = {
    "Health": health_box_img,
    "Ammo": ammo_box_img,
    "Grenade": grenade_box_img
}

font = pygame.font.SysFont("Futura", 20)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        self.is_alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.grenades = grenades
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

        # Create ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0

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
            bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1

    def ai(self):
        if self.is_alive and player.is_alive:
            if not self.idling and random.randint(1, 200) == 1:
                self.update_action(0)  # 0: idle
                self.idling = True
                self.idling_counter = 50

            # Check if the ai is near the player
            if self.vision.colliderect(player.rect):
                # Stops running and face the player
                self.update_action(0)
                self.shoot()

            else:
                if not self.idling:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False

                    ai_moving_left = not ai_moving_right
                    self.movement(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: Run
                    self.move_counter += 1
                    # Update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

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

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.is_alive = False
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_box[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        # Checks if the player picked up the box.
        if pygame.sprite.collide_rect(self, player):
            # Check kind of box
            if self.item_type == "Health":
                player.health += 25
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.item_type == "Ammo":
                player.ammo += 15
            elif self.item_type == "Grenade":
                player.grenades += 3

            # Deletes the item box
            self.kill()


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y, health, max_health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        # Update with new health
        self.health = health

        # Calculate health ratio
        ratio = self.health / self.max_health

        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 150 * ratio, 20))


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

        for enem in enemy_group:
            if pygame.sprite.spritecollide(enem, bullet_group, False):
                if enem.alive:
                    enem.health -= 25
                    self.kill()


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # Check collision with floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.speed = 0

        # Check collision with walls
        if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
            self.direction *= -1

        # Update grenade position
        self.rect.x += dx
        self.rect.y += dy

        # Countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 0.5)
            explosion_group.add(explosion)

            # Do damage to anyone that is nearby
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                player.health -= 50
            for enem in enemy_group:
                if abs(self.rect.centerx - enem.rect.centerx) < TILE_SIZE * 2 and \
                        abs(self.rect.centery - enem.rect.centery) < TILE_SIZE * 2:
                    enem.health -= 50


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"images/Shooter/explosion/exp{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        EXPLOSION_SPEED = 4

        # Update explosion animation
        self.counter += 1

        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.index += 1

            if self.index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.index]


# Sprites group
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()

# Create item boxes (temporary)
item_b = ItemBox("Health", 100, 260)
item_box_group.add(item_b)
item_b = ItemBox("Ammo", 400, 260)
item_box_group.add(item_b)
item_b = ItemBox("Grenade", 500, 260)
item_box_group.add(item_b)

# Instantiate objects
player = Soldier("player", 200, 200, 1.65, 5, 20, 5)
health_bar = HealthBar(10, 10, player.health, player.health)
enemy = Soldier("enemy", 500, 200, 1.65, 2, 20, 0)
enemy2 = Soldier("enemy", 300, 200, 1.65, 2, 20, 0)
enemy_group.add(enemy)
enemy_group.add(enemy2)

run = True
while run:
    clock.tick(fps)

    draw_bg()
    # Show player health
    health_bar.draw(player.health)

    # Show ammo, grenades, health
    draw_text(f"AMMO: ", font, WHITE, 10, 35)
    for x in range(player.ammo):
        screen.blit(bullet_img, (90 + (x * 10), 45))

    draw_text(f"GRENADES: ", font, WHITE, 10, 60)
    for x in range(player.grenades):
        screen.blit(grenade_img, (135 + (x * 15), 65))

    player.update()
    player.draw()

    for enemy in enemy_group:
        enemy.ai()
        enemy.update()
        enemy.draw()

    # Update and draw groups
    bullet_group.update()
    grenade_group.update()
    explosion_group.update()
    item_box_group.update()
    bullet_group.draw(screen)
    grenade_group.draw(screen)
    explosion_group.draw(screen)
    item_box_group.draw(screen)

    # Update player actions
    if player.is_alive:
        # Shoot bullets
        if shoot:
            player.shoot()
        # Throw grenade
        elif grenade and not is_thrown and player.grenades > 0:
            grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),
                              player.rect.top, player.direction)
            grenade_group.add(grenade)
            is_thrown = True
            player.grenades -= 1
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
            if event.key == pygame.K_q:
                grenade = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_RETURN:
                shoot = False
            if event.key == pygame.K_q:
                grenade = False
                is_thrown = False

    pygame.display.update()

pygame.quit()
