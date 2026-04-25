import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
GRAY = (128, 128, 128)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Create a screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# A function to draw a placeholder image (since we don't use external png files)
def create_surface_with_color(width, height, color):
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, surf.get_rect(), border_radius=10)
    return surf

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a red rectangle to represent the enemy car
        self.image = create_surface_with_color(40, 80, RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        # If the enemy goes off the screen, respawn it and increase score
        if (self.rect.top > SCREEN_HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a yellow circle to represent the coin
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -50)

    def move(self):
        self.rect.move_ip(0, SPEED)
        # If the coin goes off the screen, respawn it
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = -50
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a blue rectangle to represent the player car
        self.image = create_surface_with_color(40, 80, BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        # Move left
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        # Move right
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

bg_y = 0

# Game Loop
while True:
    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the scrolling background (gray road with white lane markers)
    DISPLAYSURF.fill(GRAY)
    bg_y = (bg_y + SPEED) % 100
    for i in range(-100, SCREEN_HEIGHT + 100, 100):
        pygame.draw.rect(DISPLAYSURF, WHITE, (SCREEN_WIDTH//2 - 5, i + bg_y, 10, 50))

    # Render and display scores
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    
    DISPLAYSURF.blit(score_text, (10, 10))
    # Showing the number of collected coins in the top right corner
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - coin_text.get_width() - 10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        # Stop the game, show game over screen
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
    # Check for collision between Player and Coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected_coins:
        COINS += 1
        # Respawn the collected coin at the top
        coin.rect.top = -50
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)

    pygame.display.update()
    FramePerSec.tick(FPS)