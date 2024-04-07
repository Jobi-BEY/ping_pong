from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rect.w = w
        self.rect.h = h
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def move_1(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y <500-5-self.rect.h:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    def move_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y <500-5-self.rect.h:
            self.rect.y += self.speed
        if keys[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__(img,x,y,w,h,speed)
        self.speed_x = 0
        self.speed_y = 0
    def set_direction(self,speed_x,speed_y):
        self.speed_x = 0
        self.speed_y = 0
    def rekowet(self):
        self.rect.x +=self.speed_x*self.speed
        self.rect.x +=self.speed_y*self.speed
    def check_direction():
        global score_l, score_r
        if self.rect.y <=5:
            self.speed*-1
        elif self.rect.y>=495-self.self.rect.h:
            self.speed*-1
        elif self.rect.spritecollide(player_l.rect):
            self.speed_x
        elif self.rect.spritecollide(player_r.rect):
            self.speed_x      
        elif self.rect.x <=0:
            score_r += 1
            self.rect.x = 350-self.rect.w/2
            self.rect.y = 250-self.rect.h/2
        elif self.rect.x <=700-self.rect.w:
            score_l += 1
            self.rect.x = 350-self.rect.w/2
            self.rect.y = 250-self.rect.h/2
              
player_l = Player('koral_l.png',10,210,40,100,5)
player_r = Player('koral_r.png',650,210,40,100,5)
ball = Ball('fish_fuga',325,225,50,50,10)
window = display.set_mode((700,500))
display.set_caption('saveEcoCity')
FPS = 60
score_l = 0
score_r = 0
game = True
clock = time.Clock()
background = transform.scale(image.load('sea.jpg'),(700,500))
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))

    player_l.reset()
    player_l.move_2()
    player_r.reset()
    player_r.move_1()
    ball.rekowet()
    ball.check_direction()
    ball.reset()


    display.update()
    clock.tick(FPS)