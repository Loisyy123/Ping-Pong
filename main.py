from pygame import *
from random import *
from PyQt5 import *
win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load("background.jpg"), (700, 500))
speed = 5
speed1 = 5
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed

        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += speed

    def update_l(self):
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed

        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += speed

class Ball(GameSprite):
    def update(self):
        self.rect.y == speed
        if self.rect.y > 700:
            self.rect.y > -50

Player1 = Player('raket.png', 15, 200, speed)
Player2 = Player('raket.png', 635, 200, speed1)
ball = Ball('ball.png', 100, 250, speed)

clock = time.Clock()
FPS = 60
game = True
speed_x = 3
speed_y = 3
finish = False
font.init()
font1 = font.SysFont('Arial', 35)
lose1 = font1.render('Player 1 LOSE', True, (255, 0, 0))
font2 = font.SysFont('Arial', 35)
lose2 = font2.render('Player 2 LOSE', True, (255, 0, 0))





while game:
    keys_pressed = key.get_pressed()
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(Player1, ball) or sprite.collide_rect(Player2, ball):
        speed_x *= -1 

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (250, 200))

    if ball.rect.x > 710:
        finish = True
        window.blit(lose2, (250, 200))

    ball.update()
    ball.reset()

    Player2.update_r()
    Player2.reset()

    Player1.update_l()
    Player1.reset()


    display.update()
    clock.tick(FPS)