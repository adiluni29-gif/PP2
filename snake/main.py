import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Setup Screen and Colors
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

font_small = pygame.font.SysFont("Verdana", 20)
font_large = pygame.font.SysFont("Verdana", 40)

def draw_grid():
    # Optional: Draw grid lines for better visualization
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def get_random_food_position(snake_body):
    """
    Generate random position for food, so that it does not fall on a wall or a snake.
    """
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake_body:
            return (x, y)

def main():
    # Snake starts in the middle
    snake_head = [WIDTH // 2, HEIGHT // 2]
    # Snake body is a list of [x, y] coordinates
    snake_body = [[WIDTH // 2, HEIGHT // 2], [WIDTH // 2 - BLOCK_SIZE, HEIGHT // 2], [WIDTH // 2 - 2 * BLOCK_SIZE, HEIGHT // 2]]
    
    direction = 'RIGHT'
    change_to = direction

    score = 0
    level = 1
    # Base speed
    speed = 10

    # Initial food position
    food_pos = get_random_food_position(snake_body)

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Key presses to change direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Update direction
        direction = change_to

        # Move the snake head
        if direction == 'UP':
            snake_head[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            snake_head[1] += BLOCK_SIZE
        if direction == 'LEFT':
            snake_head[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            snake_head[0] += BLOCK_SIZE

        # Insert new head position into the snake body
        snake_body.insert(0, list(snake_head))

        # Check if food is eaten
        if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
            score += 1
            # Level up every 4 foods
            if score % 4 == 0:
                level += 1
                # Increase speed when the user passes to the next level
                speed += 2
            
            # Generate new food position
            food_pos = get_random_food_position(snake_body)
        else:
            # If food is not eaten, remove the tail so the snake doesn't grow infinitely
            snake_body.pop()

        # Checking for border (wall) collision and whether the snake is leaving the playing area
        if snake_head[0] < 0 or snake_head[0] >= WIDTH or snake_head[1] < 0 or snake_head[1] >= HEIGHT:
            game_over_screen()

        # Check if the snake hit itself
        for block in snake_body[1:]:
            if snake_head[0] == block[0] and snake_head[1] == block[1]:
                game_over_screen()

        # Draw everything
        screen.fill(BLACK)
        draw_grid()

        # Draw snake
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw food
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # Add counter to score and level
        score_text = font_small.render(f"Score: {score}", True, WHITE)
        level_text = font_small.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (WIDTH - 100, 10))

        pygame.display.update()
        clock.tick(speed)

def game_over_screen():
    """
    Display game over text and wait before quitting
    """
    game_over_text = font_large.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()