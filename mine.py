import pygame as pg
import random
pg.init()
win_width, win_height = 800, 600
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("pin pong")
class GameSprite:
    def __init__(self, image, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def control1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s] and self.rect.y < 600-250:
            self.rect.y += self.speed
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def control2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] and self.rect.y < 600-250:
            self.rect.y += self.speed
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def move(self):
        global x2, y2, player1, player2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(player2, self):
            x2 = -2
        if pg.sprite.collide_rect(player1, self):
            x2 = 2
        if self.rect.y < 0:
            y2 = 2
        if self.rect.y > 575:
            y2 = -2
x2, y2 = 2, 2

back = GameSprite("fon.jpg", 0, 0, 800, 600, 0)
player1 = Player("stick2.png",0, 300, 20, 250, 3)
player2 = Player("stick1.png",780, 300, 20, 250, 3)
ball = Ball("ball.png", 400, 300, 25, 25, 5)
game =  True
score1 = 0
score2 = 0 
while game:
    pg.time.Clock().tick(144)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    if ball.rect.x < 0:
        score1 +=1 
        ball.rect.x = 400
    if score1 >= 3:
        game = False
    if ball.rect.x < 0:
        score2 +=1 
        ball.rect.x = 400
    if score2 >= 3:
        game = False
    if ball.rect.x > 800:
        score2 +=1 
        ball.rect.x = 400
    back.reset()
    player1.reset()
    player1.control1()
    player2.control2()
    player2.reset()
    ball.reset()
    ball.move()
    pg.display.flip()