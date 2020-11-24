import pygame, sys, random
from SnakePart import snake, apple

LIGHTGREEN = (30, 255, 0)
RED =(255, 0, 0)
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class body(pygame.sprite.Sprite):
    def __init__(self, food, head):
        super().__init__()
        self.list = []
        self.food = food
        self.head = head
    def create_segment():
        new_segment
  
    def add(self):
        if self.head.colliderect(self.food):
            self.list.append(create_segment())

randomX = random.randrange(10, 580, 5)
randomY = random.randrange(10, 580, 5)

pygame.init()
clock = pygame.time.Clock()
w = 600
h = 600
screen = pygame.display.set_mode([w, h])

all_sprites_list = pygame.sprite.Group()
 
snake = snake(LIGHTGREEN, 20, 20)
snake.rect.x = 10
snake.rect.y = 10

apple = apple(RED, 20, 20)
apple.rect.x = randomX
apple.rect.y = randomY
 
all_sprites_list.add(snake)
all_sprites_list.add(apple)

engine = True
clock = pygame.time.Clock()
while engine:
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                engine=False

    all_sprites_list.update()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit