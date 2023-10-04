from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wl_width, wl_height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wl_width
        self.height = wl_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font = font.SysFont('Arial',70)
win = font.render("YOU WON!", True, (255, 215, 0))
lose = font.render("YOU LOST...", True, (255, 215, 0))

win_width = 700
win_height = 500
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(win_width,win_height))

FPS = 60
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()



player = Player('hero.png', 5, win_height - 80, 4)
enemy = Enemy('cyborg.png',win_width - 80, 200, 2)
treasure = GameSprite('treasure.png', win_width-120, win_height - 80, 0)
w1 = Wall(119,119,0,150,15,100,200)
w2 = Wall(119,119,0,200,15,250,300)
w3 = Wall(119,119,0,250,15,300,450)

finish = False
game = True 

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    if finish == False:
        window.blit(background, (0,0))
        player.reset()
        enemy.reset()
        treasure.reset()
        player.update()
        enemy.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        if sprite.collide_rect(player,enemy) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            window.blit(lose, (200,200))
            finish = True
            mixer.music.load('kick.ogg')
            mixer.music.play()
        if sprite.collide_rect(player, treasure):
            window.blit(win, (200,200))
            finish = True
            mixer.music.load('money.ogg')
            mixer.music.play()    
        
    
    
    
    
    
    display.update()
    clock.tick(FPS)