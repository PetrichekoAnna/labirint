#создай игру "Лабиринт"!
from pygame import *

#создай окно игры

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
backgroud = transform.scale(image.load('background.jpg') , (700, 500))



#задай фон сцены

#создай 2 спрайта и р

#обработай событие «клик по кнопке "Закрыть окно"»
#! x1 = 100 
#?y1 = 300
#* x2 = 400 
# TODO y2 = 400 

clock = time.Clock()

class gameSprite(sprite.Sprite):
    def __init__(self, images, x, y, speed ):
        super().__init__()
        self.image = transform.scale(image.load(images), (70, 70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def reset(self):
        window.blit(self.image,  (self.rect.x, self.rect.y))

class Player(gameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 695:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

class Enemy(gameSprite):
    derection = 'left'
    def update(self):
        if self.rect.x < 470:
            self.derection = 'right'
        if self.rect.x > 620:
            self.derection = 'left'
        if self.derection == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_height = wall_height
        self.wall_width = wall_width
        self.image = Surface((self.wall_height, self.wall_width))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def drawWall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



player = Player('hero.png', 60, 60, 5)
monster = Enemy('cyborg.png', 610, 280, 4)
win = gameSprite('treasure.png', 500, 400, 0)
wall_1 = Wall(255, 222, 164, 450, 5, 50, 10)
wall_2 = Wall(255, 222, 164, 5, 250, 50, 10)
wall_3 = Wall(255, 222, 164, 450, 5, 250, 100)
wall_4 = Wall(255, 222, 164, 5, 250, 350, 170)
wall_5 = Wall(255, 222, 164, 250, 5, 450, 250)
#wall_6 = Wall(255, 222, 164, 5, 250, 350, 170)


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font. init()
font = font.Font(None, 70)
wins = font.render(
    'YOU WIN!' , True, (255, 200, 100)
)

lose = font.render(
    'YOU LOSE!' , True, (255, 40, 20)
)

finish = False


game = True
while game:


    for e in event.get():
        if e.type ==  QUIT:
            game = False 
        
    if finish != True:

        window.blit(backgroud , (0, 0))

        player.reset()
        monster.reset() 
        win.reset()

        player.update()
        monster.update() 
        wall_1.drawWall()
        wall_2.drawWall()
        wall_3.drawWall()
        wall_4.drawWall()
        wall_5.drawWall()

        if sprite.collide_rect(player, win):
            finish = True 
            window.blit(wins, (200, 200))
            money.play() 
        if sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4) or sprite.collide_rect(player, wall_5) or sprite.collide_rect(player, monster):
            finish = True 
            window.blit(lose, (200, 200))
            kick.play()
        

    clock.tick(60)
    display.update() 
            