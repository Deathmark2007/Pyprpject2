import pygame, sys, random
from SnakePart import snake, apple
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

randomX = random.randrange(10, 390, 5)
randomY = random.randrange(10, 490, 5)

#font = pygame.font.Font('freesansbold.ttf', 20)
#text = font.render("Hi", True, BLACK, GREEN)
#textRect = text.get_rect()  
#textRect.center = (300, 20) 

SCREENWIDTH=400
SCREENHEIGHT=500
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

all_sprites_list = pygame.sprite.Group()
 
snake = snake(GREEN, 20, 20)
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
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     engine=False
    

    all_sprites_list.update()
    screen.fill(BLACK)
    #screen.blit(text, textRect) 
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit