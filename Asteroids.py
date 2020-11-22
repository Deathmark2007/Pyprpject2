import pygame, sys, random

class ship(pygame.sprite.Sprite):
    def __init__(self, image, ):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = (300, 300))
        self.angle = 0

    def turn(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.angle += 1
                print('right')

            if event.key == pygame.K_LEFT:
                self.angle -= 1
                print('left')

    def update(self):
        self.turn()

class asteroids(pygame.sprite.Sprite):
    def __init__(self, image, x_speed, y_speed, ship):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = (300, 200))
        self.x_speed = x_speed * random.choice((-1.5, -1,-0.5, 0.5, 1, 1.5))
        self.y_speed = y_speed * random.choice((-1,-0.5, 0.5, 1))
        self.ship = ship


    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def borders(self):
        if self.rect.top <= 0 or self.rect.bottom >= h:
            self.y_speed *= -1

        if self.rect.left <= 0 or self.rect.right >= w:
            self.x_speed *= -1

    def update(self):
        self.move()
        self.borders()

pygame.init()
clock = pygame.time.Clock()
w = 600
h = 600
screen = pygame.display.set_mode([w, h])

background = pygame.image.load('space_background.jpeg').convert()
bg_surface = pygame.transform.scale2x(background)
bg = pygame.transform.scale2x(bg_surface)

player = ship('ship.bmp')
player_group = pygame.sprite.Group()
player_group.add(player)

asteroid = asteroids('asteroids.png',4,4,player_group)
asteroid_sprites = pygame.sprite.Group()
asteroid_sprites.add(asteroid)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0,0))
    player_group.draw(screen)
    player.update()

    asteroid_sprites.draw(screen)
    asteroid.update()

    pygame.display.flip()
    clock.tick(120)

    pygame.display.flip