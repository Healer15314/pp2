import math
import pickle
import pygame
import random
import sys
import time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
# RGB (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 20, 147)
GRAY = (128, 128, 128)


WIDTH = 800
HEIGHT = 650

size = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

background = pygame.image.load("Images/backgr.png")
font = pygame.font.Font('JosefinSans-Bold.ttf', 15)
wallphot = pygame.image.load("Images/wall.png")



color = WHITE
x = 100
y = 100
dx = 1
dy = 0
choose = 0

snakes = list()
wall = list()
wall_hard = list()
done = False
velocity = 25
Score = 0
game_over = False
players_cnt = 0
level = 1


class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[412, 412]]
        self.radius = 12.5
        self.x = self.elements[0][0]
        self.y = self.elements[0][1]
        self.dx = 25
        self.dy = 0
        self.score = 0
        self.is_add = False
        self.level = 1
        self.maxspeed = 8

    def draw(self):
        for i in self.elements:
            pygame.draw.circle(screen, PINK , i, self.radius)

    def add_element(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.score >= 10:
            self.level = 2

    def move(self):
        if self.is_add:
            self.add_element()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


class Food:
    def __init__(self):
        self.image = pygame.image.load("Images/apple.png")
        self.x = random.randrange(25, 740, 25)
        self.y = random.randrange(25, 535, 25)
        while (self.x, self.y) in wall or (self.x, self.y) in wall_hard:
            self.x = random.randrange(25, 740, 25)
            self.y = random.randrange(25, 535, 25)
        self.elements = [[100, 100]]
        self.rect = 10

    def draw(self):
        for self.element in self.elements:
            screen.blit(self.image, (self.x, self.y))


food = Food()


def is_collision(snake):
    global game_over
    if (snake.elements[0][0] - 12.5 <= food.x < snake.elements[0][0] + 12.5 and (
            snake.elements[0][1] - 12.5 <= food.y <= snake.elements[0][1] + 12.5)):
        snake.is_add = True
        snake.score += 1
        food.x = random.randrange(25, 750, 25)
        food.y = random.randrange(25, 550, 25)
        if level == 2:
            while (food.x, food.y) in wall or (food.x, food.y) in wall_hard or (
                    food.x + 12.5, food.y + 12.5) in snake.elements:
                food.x = random.randrange(25, 740, 25)
                food.y = random.randrange(25, 535, 25)
        else:
            while (food.x, food.y) in wall or (food.x + 12.5, food.y + 12.5) in snake.elements:
                food.x = random.randrange(25, 740, 25)
                food.y = random.randrange(25, 535, 25)
   


def collision(a, b):
    global game_over
    if a[0] in b[1:]:
        game_over = True
    if b[0] in a[1:]:
        game_over = True


def render(surface, text, size, x, y, clr):
    font = pygame.font.Font('JosefinSans-Bold.ttf', size)
    text_surface = font.render(text, True, clr)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def start_menu():
    global choose
    menu = True
    while menu:
        screen.blit(background, (0, 0))
        
        render(screen, "START", 25, WIDTH / 2, HEIGHT / 2.5, WHITE)
         
        pygame.display.flip()
        FramePerSec.tick(FPS)
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
            if key.type == pygame.KEYDOWN and key.key == K_DOWN:
                if choose != 1:
                    choose += 1
            if key.type == pygame.KEYDOWN and key.key == K_UP:
                if choose != 0:
                    choose -= 1
            if key.type == pygame.KEYDOWN and key.key == K_RETURN:
                if choose == 0:
                    player(1)
                else:
                    player(2)


def player(cnt):
    global level
    choose = 0
    while True:
        screen.blit(background, (0, 0))
        if choose == 0:
            render(screen, "I AM READY", 25, WIDTH / 1.9, HEIGHT / 2.5, WHITE)
            render(screen, "CONTINUE", 25, WIDTH / 2, HEIGHT / 2, WHITE)
        else:
            render(screen, "I AM READY", 25, WIDTH / 2, HEIGHT / 2.5, WHITE)
            render(screen, "CONTINUE", 25, WIDTH / 1.9, HEIGHT / 2, WHITE)
        pygame.display.flip()
        FramePerSec.tick(FPS)
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
            if key.type == pygame.KEYDOWN and key.key == K_DOWN:
                if choose != 1:
                    choose += 1
            if key.type == pygame.KEYDOWN and key.key == K_UP:
                if choose != 0:
                    choose -= 1
            if key.type == pygame.KEYDOWN and key.key == K_RETURN:
                if choose == 1:
                    load(cnt)
                game(cnt)


for i in range(0, 801, 25):
    wall.append((i, 0))
    wall.append((i, 575))
for i in range(25, 575, 25):
    wall.append((0, i))
    wall.append((775, i))
for i in range(100, 226, 25):
    wall_hard.append((i, 100))
    wall_hard.append((i, 500))
    wall_hard.append((i + 450, 100))
    wall_hard.append((i + 450, 500))
for i in range(125, 226, 25):
    wall_hard.append((100, i))
    wall_hard.append((675, i))
    wall_hard.append((100, i + 250))
    wall_hard.append((675, i + 250))


def walls(level):
    for i in wall:
        screen.blit(wallphot, i)
    if level == 2:
        for i in wall_hard:
            screen.blit(wallphot, i)


def wall_collision(x1, y1, wall):
    global game_over
    for i in wall:
        distance = math.sqrt(math.pow(i[0] + 12.5 - x1, 2) + math.pow(i[1] + 12.5 - y1, 2))
        if distance < 12:
            game_over = True


is_change = True


def dump(file, file1, cnt):
    with open('data.pkl', 'bw') as f:
        pickle.dump(file, f)
        pickle.dump((file1.x, file1.y), f)


def load(cnt):
    global food, snakes, is_change
    with open('data.pkl', 'br') as f:
        snakes = pickle.load(f)
        (food.x, food.y) = pickle.load(f)
        if snakes[0].level == 2:
            is_change = False


tick = 10


def game(cnt):
    global snakes, food, game_over, level, is_change
    for i in range(cnt):
        if len(snakes) >= cnt:
            continue
        else:
            snakes.append(Snake())
    while not game_over:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if len(snakes) == 1:
                snake = snakes[0]
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    snake.dx = 0
                    if snake.dy != velocity or snake.size == 1:
                        snake.dy = -velocity
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    snake.dx = 0
                    if snake.dy != -velocity or snake.size == 1:
                        snake.dy = velocity
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    if snake.dx != -velocity or snake.size == 1:
                        snake.dx = velocity
                    snake.dy = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    if snake.dx != velocity or snake.size == 1:
                        snake.dx = -velocity
                    snake.dy = 0

               
        walls(level)
        score1 = font.render("SCORE: " + str(snakes[0].score), True, WHITE)
        screen.blit(score1, (320, 600))
        
        for snake in snakes:
            tick = snake.maxspeed
            snake.move()
            snake.draw()
            level = max(snake.level, level)
            if level == 2 and is_change:
                time.sleep(0.5)
                snake.size = 1
                snake.elements = [[412, 412]]
                snake.maxspeed = 13
                snake.dx = 0
                snake.dy = 0
                is_change = False
            is_collision(snake)
            if not ((25 <= snake.elements[0][0] <= 775) and (25 <= snake.elements[0][1] <= 575)):
                pygame.quit()
                sys.exit()
            if level == 2:
                wall_collision(snake.elements[0][0], snake.elements[0][1], wall_hard)
        food.draw()
        # pygame.display.flip()
        clock.tick(tick)
        pygame.display.update()
    dump(snakes, food, cnt)
    pygame.quit()


start_menu() 