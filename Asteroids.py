import pygame

class ship(pygame.sprite.Sprite):
    def __init__(self):
        # the ship image (we're using images)
        self.image = pygame.image.load('ship.bmp')
    def turn_right(self):
        #detecting the keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                #we'll use rotozoom to rotate the ship.

pygame.init()
clock = pygame.time.Clock()


w = 600
h = 600
screen = pygame.display.set_mode([w, h])

while True:
    for event in pygame.event.get():
        if even.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip