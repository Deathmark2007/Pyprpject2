import pygame, random, sys
#Let's import the Car Class
from DodgeParts import Car, Debree
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
DEBREECOLOR = (75, 0, 15)

Points = 0

randomX = random.randrange(110, 190, 10)


#font = pygame.font.Font('freesansbold.ttf', 20)
#text = font.render(str(speed), True, BLACK, GREEN)
#textRect = text.get_rect()  
#textRect.center = (x, y) 
        
SCREENWIDTH=400
SCREENHEIGHT=500
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")
 
all_sprites_list = pygame.sprite.Group()
 
playerCar = Car(RED, 20, 30)
playerCar.rect.x = 240
playerCar.rect.y = 300

Debree = Debree(DEBREECOLOR, 20, 30)
Debree.rect.x = randomX
Debree.rect.y = 0
 
all_sprites_list.add(playerCar)

carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     carryOn=False
 
        keys = pygame.key.get_pressed()
        
        #if keys[pygame.K_LEFT]:
        #    playerCar.moveLeft(5)
        #if keys[pygame.K_RIGHT]:
        #    playerCar.moveRight(5)
        #if keys[pygame.K_UP]:
        #    playerCar.moveUp(5)
        #if keys[pygame.K_DOWN]:
        #    playerCar.moveDown(5)
        
        randomX += 5
        Debree.rect.x = randomX
        if randomX == 500:
            Debree.rect.x = randomX
            Debree.rect.y = 0
            
        if keys[pygame.K_a]:

            playerCar.moveLeft(5)
        if keys[pygame.K_d]:
            playerCar.moveRight(5)
        if keys[pygame.K_w]:
            playerCar.moveUp(5)
        if keys[pygame.K_s]:
            playerCar.moveDown(5)

        #if playerCar.rect.x and playerCar.rect.x + 20 and playerCar.rect.y and playerCar.rect.y + 30
        
        all_sprites_list.update()
        screen.fill(GREEN)
        pygame.draw.rect(screen, GREY, [100,50, 200,500])
        pygame.draw.line(screen, WHITE, [198,50],[198,550],4)
        
        #screen.blit(text, textRect)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
 
pygame.quit() 