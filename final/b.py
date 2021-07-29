import pygame
import random

from pygame.constants import BLEND_ALPHA_SDL2

# Initialize pygame program
pygame.init()

# Surface
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("First game")
nurik = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
font = pygame.font.Font('JosefinSans-Bold.ttf', 15)

running = True

clock = pygame.time.Clock()
# Frames Per Second
FPS = 60

x, y = 200, 20
dx, dy = 0, 0


class Ball:
  def __init__(self, *args, **kwargs):
    self.size = 25
    self.x = random.randint(0, SCREEN_WIDTH - self.size)
    self.y = random.randint(0, SCREEN_HEIGHT - self.size)
    self.dx = random.randint(0,0)
    self.dy = random.randint(0, 0)
    self.score = 0
    self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

  def move(self):
    self.x += self.dx
    self.y += self.dy
    

  def draw(self):
    pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.size, self.size))
balls = [Ball()]

class Food:
    def __init__(self):
        self.image = pygame.image.load("Images/poi.png")
        self.x = random.randrange(25, 740, 25)
        self.y = random.randrange(25, 535, 25)
        while (self.x, self.y) in (balls[0].x,balls[0].y):
            self.x = random.randrange(25, 740, 25)
            self.y = random.randrange(25, 535, 25)
        self.elements = [[100, 100]]
        
        self.rect = 10

    def draw(self):
        for self.element in self.elements:
            screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += random.randint(-6, 6 )
        self.y += random.randint(-6, 6)
def is_collision(ball):
    global game_over,nurik
    for food in foods:
      if (ball.x - 25 <= food.x < ball.x + 25 and (ball.y - 25 <= food.y <= ball.y + 25)):
          ball.score += 1
          food.x = random.randrange(25, 750, 25)
          food.y = random.randrange(25, 550, 25)
          while (food.x, food.y) in (balls[0].x,balls[0].y) and (food.x, food.y) in (poisons[0].x,poisons[0].y):
              food.x = random.randrange(25, 740, 25)
              food.y = random.randrange(25, 535, 25)
    for poison in poisons:
      if (ball.x - 25 <= poison.x < ball.x + 25 and (ball.y - 25 <= poison.y <= ball.y + 25)):
        if(ball.score<0):
          nurik = False
          ball.score -=1
          poison.x = random.randrange(25, 750, 25)
          poison.y = random.randrange(25, 550, 25)
          while (poison.x, poison.y) in (balls[0].x,balls[0].y) and (poison.x, poison.y) in (foods[0].x,foods[0].y):
              poison.x = random.randrange(25, 740, 25)
              poison.y = random.randrange(25, 535, 25)
      

foods = [Food()]
for x in range(30):
      foods.append(Food())


class Poison:
    def __init__(self):
        self.image = pygame.image.load("Images/apple.png")
        self.x = random.randrange(25, 740, 25)
        self.y = random.randrange(25, 535, 25)
        while (self.x, self.y) in (balls[0].x,balls[0].y) and (self.x, self.y) in (foods[0].x,foods[0].y):
            self.x = random.randrange(25, 740, 25)
            self.y = random.randrange(25, 535, 25)
        self.elements = [[100, 100]]
        
        self.rect = 10

    def draw(self):
        for self.element in self.elements:
            screen.blit(self.image, (self.x, self.y))
    
    def move(self):
        self.x += random.randint(-6, 6 )
        self.y += random.randint(-6, 6)
poisons = [Poison()]
for x in range(30):
      poisons.append(Poison())



def render(surface, text, size, x, y, clr):
    font = pygame.font.Font('JosefinSans-Bold.ttf', size)
    text_surface = font.render(text, True, clr)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Main loop
while running:
  # Event loop

  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        balls[0].dx = 0
        balls[0].dy = -3
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        balls[0].dx = 0
        balls[0].dy = 3
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        balls[0].dx = 3
        balls[0].dy = 0            
    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        balls[0].dx = -3
        balls[0].dy = 0          
  screen.fill(WHITE)
  for ball in balls:
    ball.move()
    ball.draw()
    is_collision(ball)

  for poison in poisons:
    poison.move()
  for food in foods:
    food.move()
  
  score1 = font.render("SCORE: " + str(balls[0].score), True, BLACK)
  screen.blit(score1, (20, 20))
  
  for food in foods:
    food.draw()
  for poison in poisons:
    poison.draw()

 
 

  pygame.display.flip()

  clock.tick(FPS)


pygame.quit()