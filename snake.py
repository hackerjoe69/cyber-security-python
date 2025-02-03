import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display variables
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"

# Food properties
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

# Game variables
score = 0

# Set up font
font_style = pygame.font.SysFont(None, 30)

def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width // 2 - len(msg) * 12, height // 2])

def game_loop():
    global direction, score, snake_pos, snake_body, food_pos

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

        # Move snake
        head = []
        head.append(snake_pos[0])
        head.append(snake_pos[1])

        if direction == "LEFT":
            head[0] -= 10
        elif direction == "RIGHT":
            head[0] += 10
        elif direction == "UP":
            head[1] -= 10
        elif direction == "DOWN":
            head[1] += 10

        snake_pos = head.copy()
        snake_body.append(snake_pos)

        # Check if snake has hit itself or wall
        if (snake_pos in snake_body[:-1] or
                snake_pos[0] < 0 or snake_pos[0] >= width or
                snake_pos[1] < 0 or snake_pos[1] >= height):
            message("Game Over", RED)
            pygame.display.update()
            pygame.time.wait(2000)
            break

        # Check if snake has eaten food
        if snake_pos == food_pos:
            score += 1
            food_pos = [random.randrange(1, (width//10)) * 10,
                        random.randrange(1, (height//10)) * 10]
        else:
            snake_body.pop(0)  # Remove the last piece of the tail

        screen.fill(BLACK)
        draw_snake(snake_body)
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        message(f"Score: {score}", WHITE)

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

game_loop()
