from pygame import *
from random import *
window = display.set_mode((700, 500))
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
        
Player1 = Player('raket.jpg', 15, 200, speed)
Player2 = Player('raket.jpg', 635, 200, speed1)

clock = time.Clock()
FPS = 60
game = True


while game:
    keys_pressed = key.get_pressed()
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False




    Player2.update_r()
    Player2.reset()

    Player1.update_l()
    Player1.reset()


    display.update()
    clock.tick(FPS)