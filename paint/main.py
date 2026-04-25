import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

COLORS = [BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]

# Canvas surface to draw persistently
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# UI Parameters
UI_HEIGHT = 60
TOOL_Y = 10
COLOR_Y = 10

# Current State
current_color = BLACK
current_tool = "pen"  # "pen", "eraser", "rect", "circle"
radius = 5

font = pygame.font.SysFont("Verdana", 15)

def draw_ui():
    # Background for UI
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, UI_HEIGHT))
    
    # Draw tools buttons
    tools = ["pen", "eraser", "rect", "circle"]
    tool_x = 10
    for t in tools:
        color = (150, 150, 150) if current_tool == t else (220, 220, 220)
        btn_rect = pygame.Rect(tool_x, TOOL_Y, 60, 40)
        pygame.draw.rect(screen, color, btn_rect)
        pygame.draw.rect(screen, BLACK, btn_rect, 2) # border
        
        text = font.render(t, True, BLACK)
        screen.blit(text, (tool_x + 5, TOOL_Y + 10))
        tool_x += 70

    # Draw color buttons
    color_x = tool_x + 50
    for c in COLORS:
        btn_rect = pygame.Rect(color_x, COLOR_Y, 40, 40)
        pygame.draw.rect(screen, c, btn_rect)
        if current_color == c:
            pygame.draw.rect(screen, BLACK, btn_rect, 3) # highlight selected
        color_x += 50

def handle_ui_click(pos):
    global current_tool, current_color
    x, y = pos
    if y <= UI_HEIGHT:
        # Check tool click
        tool_x = 10
        tools = ["pen", "eraser", "rect", "circle"]
        for t in tools:
            if tool_x <= x <= tool_x + 60:
                current_tool = t
                return True
            tool_x += 70
        
        # Check color click
        color_x = tool_x + 50
        for c in COLORS:
            if color_x <= x <= color_x + 40:
                current_color = c
                return True
            color_x += 50
    return False

def main():
    clock = pygame.time.Clock()
    drawing = False
    start_pos = None
    last_pos = None

    while True:
        # We blit canvas first, then draw preview or UI on top
        screen.blit(canvas, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    if not handle_ui_click(event.pos):
                        drawing = True
                        start_pos = event.pos
                        last_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    end_pos = event.pos
                    # Finalize rectangle or circle
                    if current_tool == "rect":
                        x1, y1 = start_pos
                        x2, y2 = end_pos
                        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                        pygame.draw.rect(canvas, current_color, rect, radius)
                    elif current_tool == "circle":
                        x1, y1 = start_pos
                        x2, y2 = end_pos
                        dist = math.hypot(x2 - x1, y2 - y1)
                        pygame.draw.circle(canvas, current_color, start_pos, int(dist), radius)

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if current_tool == "pen":
                        # Draw line on canvas for pen
                        pygame.draw.line(canvas, current_color, last_pos, event.pos, radius * 2)
                        # Also draw a circle to make it look smoother
                        pygame.draw.circle(canvas, current_color, event.pos, radius)
                        last_pos = event.pos
                    elif current_tool == "eraser":
                        # Eraser draws with white color
                        pygame.draw.line(canvas, WHITE, last_pos, event.pos, radius * 2)
                        pygame.draw.circle(canvas, WHITE, event.pos, radius)
                        last_pos = event.pos

        # Real-time preview for rectangle and circle
        if drawing:
            mouse_pos = pygame.mouse.get_pos()
            if current_tool == "rect":
                x1, y1 = start_pos
                x2, y2 = mouse_pos
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, current_color, rect, radius)
            elif current_tool == "circle":
                dist = math.hypot(mouse_pos[0] - start_pos[0], mouse_pos[1] - start_pos[1])
                pygame.draw.circle(screen, current_color, start_pos, int(dist), radius)

        # Draw UI
        draw_ui()

        pygame.display.flip()
        clock.tick(120)

if __name__ == "__main__":
    main()