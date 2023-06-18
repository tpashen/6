#створи гру "Лабіринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
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
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 650:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700,500))
display.set_caption("Лабiринт")
background = transform.scale(image.load("background.jpg"),(700,500))

game = True
clock = time.Clock()
FPS = 60
finish = False

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

player = Player('hero.png',10,400,5)
monster = Enemy('cyborg.png',350,250,5)
final=GameSprite("treasure.png",600,400,0)

w1 = Wall(0, 225, 0, 100, 20, 600, 10)
w2 = Wall(0, 225, 0, 100, 480, 600, 10)
w3 = Wall(0, 225, 0, 100, 100, 200, 10)
w4 = Wall(0, 225, 0, 200, 200, 200, 10)
w5 = Wall(0, 225, 0, 100, 300, 200, 10)
w6 = Wall(0, 225, 0, 100, 30, 10, 270)
w7 = Wall(0, 225, 0, 400, 100, 10, 390)
w8 = Wall(0, 225, 0, 100, 390, 300, 10)

while game:
    window.blit(background,(0, 0))
    player.reset()
    player.update()
    monster.reset()
    monster.update()
    final.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    w8.draw_wall()
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if (sprite.collide_rect(player, w1)
        or sprite.collide_rect(player, w2)
        or sprite.collide_rect(player, w3)
        or sprite.collide_rect(player, w4)
        or sprite.collide_rect(player, w5)
        or sprite.collide_rect(player, w6)
        or sprite.collide_rect(player, w7)
        or sprite.collide_rect(player, w8)):
        player.rect.x=50
        player.rect.y=400

    if sprite.collide_rect(player, monster):
        window.blit(lose, (200, 200))
        kick.play()
        finish = True

    if sprite.collide_rect(player, final):
        window.blit(win, (200, 200))
        money.play()
        finish = True
    display.update()
    clock.tick(FPS)
