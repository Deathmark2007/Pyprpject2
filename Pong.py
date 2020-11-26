import pygame, sys, random

class ball(pygame.sprite.Sprite):
    def __init__(self, image, x_speed, y_speed, paddles):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=(300, 300))
        self.x_speed = x_speed * random.choice((-1, -0.5, 0.5, 1))
        self.y_speed = y_speed * random.choice((-1, -0.5, 0.5, 1))
        self.paddle = paddles

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def borders(self):
        if self.rect.top <= 0 or self.rect.bottom >= h:
            self.y_speed *= -1


    def hit_paddle(self):
        if pygame.sprite.spritecollide(self, self.paddle, False):
            collision_point = pygame.sprite.spritecollide(self, self.paddle, False)[0].rect
            if abs(self.rect.right - collision_point.left) < 10:
                self.x_speed *= -1
            if abs(self.rect.left - collision_point.right) < 10:
                self.x_speed *= -1
            if abs(self.rect.top - collision_point.bottom) < 10:
                self.rect.top = collision_point.bottom
                self.y_speed *= -1
            if abs(self.rect.bottom - collision_point.top) < 10 and self.y_speed > 0:
                self.rect.bottom = collision_point.top
                self.y_speed *= -1



    def update(self):
        self.move()
        self.borders()
        self.hit_paddle()

class paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Paddle.png')
        self.rect = self.image.get_rect(center = (580, 300))

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.rect.y -= 7
            if event.key == pygame.K_DOWN:
                self.rect.y += 7

    def border(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= h:
            self.rect.bottom = h

    def update(self):
        self.move()
        self.border()

class opponent(pygame.sprite.Sprite):
    def __init__(self, ball):
        super().__init__()
        self.image = pygame.image.load('Paddle.png')
        self.rect = self.image.get_rect(center = (20, 300))
        self.ball = ball

    def AI(self):
        if self.rect.bottom < self.ball.rect.y:
            self.rect.y += 7
        if self.rect.top > self.ball.rect.y:
            self.rect.y -= 7

    def border(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= h:
            self.rect.bottom = h

    def update(self):
        self.AI()
        self.border()

class game_manager:
    def __init__(self, player, opponent, ball):
        self.player = player
        self.opponent = opponent
        self.ball = ball

    def score(self):
        if self.ball.rect.left <= 0:
            self.ball.rect.center = (300, 300)
            self.opponent.rect.y = 300
            self.player.rect.y = 300

        if self.ball.rect.right >= w:
            self.ball.rect.center = (300, 300)
            self.opponent.rect.y = 300
            self.player.rect.y = 300

    def update(self):
        self.score()


player = paddle()
paddle_group = pygame.sprite.Group()
paddle_group.add(player)

ping_pong = ball('Ball.png', 6, 6, paddle_group)
ball_group = pygame.sprite.Group()
ball_group.add(ping_pong)

Opponent = opponent(ping_pong)
paddle_group.add(Opponent)

manager = game_manager(player, Opponent, ping_pong)

pygame.init()
clock = pygame.time.Clock()
w = 600
h = 600
screen = pygame.display.set_mode(([w, h]))
bg_color = pygame.Color('#2F373F')
light_grey = (200, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(bg_color)
    pygame.draw.aaline(screen, light_grey, (w / 2, 0), (w / 2, h))

    ball_group.draw(screen)
    paddle_group.draw(screen)

    ping_pong.update()
    player.update()
    Opponent.update()
    manager.update()


    pygame.display.flip()
    clock.tick(60)