import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 50
dis_height = 50

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 1
snake_speed = 2

font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("bahnschrift", 15)


def Your_score(score):
    value = score_font.render("score: " + str(score), True, red)
    dis.blit(value, [5, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [10, 20])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = random.randint(12, 38)
    foody = random.randint(12, 38)

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("LOST", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        mouse = pygame.mouse.get_pos()

        if 0 <= mouse[0] <= 10 and 10 <= mouse[1] <= 40:
            # left
            x1_change = -snake_block
            y1_change = 0
        elif 40 <= mouse[0] <= 50 and 10 <= mouse[1] <= 40:
            # right
            x1_change = snake_block
            y1_change = 0
        elif 10 <= mouse[0] <= 40 and 0 <= mouse[1] <= 10:
            # up
            y1_change = -snake_block
            x1_change = 0
        elif 10 <= mouse[0] <= 40 and 40 <= mouse[1] <= 50:
            # down
            y1_change = snake_block
            x1_change = 0

        # out of bounds -> death
        if x1 >= 40 or x1 < 10 or y1 >= 40 or y1 < 10:
            game_close = True

        # move the snake
        x1 += x1_change
        y1 += y1_change

        # fill the background
        dis.fill(blue)

        # draw the food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # draw border
        pygame.draw.rect(dis, black, [10, 10, 1, 30])
        pygame.draw.rect(dis, black, [39, 10, 1, 30])
        pygame.draw.rect(dis, black, [10, 10, 30, 1])
        pygame.draw.rect(dis, black, [10, 39, 30, 1])

        # draw direction controllers
        pygame.draw.rect(dis, white, [10, 0,  30, 10])
        pygame.draw.rect(dis, white, [10, 40, 30, 10])
        pygame.draw.rect(dis, white, [0,  10, 10, 30])
        pygame.draw.rect(dis, white, [40, 10, 10, 30])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = random.randint(12, 38)
            foody = random.randint(12, 38)
            Length_of_snake += 1

        print(foodx, foody)

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

'''
foodx = random.randint(11, 39)
foody = random.randint(11, 39)
'''
