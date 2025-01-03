import pygame
import time
import random

pygame.init()

# Fenstergröße
width = 800
height = 600

# Farben
white = (255, 255, 255)
black = (0, 0, 0)

# Spielfeld
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Geschwindigkeit der Schlange
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    # Länge der Schlange
    snake_List = []
    Length_of_snake = 1

    # Position des Essens
    foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, height - 10) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            gameDisplay.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [x1, y1, 10, 10])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(gameDisplay, black, [x[0], x[1], 10, 10])

        pygame.draw.rect(gameDisplay, black, [foodx, foody, 10, 10])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, height - 10) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()