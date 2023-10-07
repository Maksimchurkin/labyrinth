#ping_pong
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player.speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = keys.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200,255,255)
win_width = 500
win_height = 600

window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('rocket.png', 30,200,4,50,150)
racket2 = Player('rocket.png', 520, 200,4,50,150)

font.init()
font1 = Font(None,36)

lose1 = render('PLAYER 1 HAS LOST!', True (100,0,0))
lose2 = render('PLAYER 2 HAS LOST!', True (100,0,0))
















if sprite.collide_rect(racket1, ball) or 

