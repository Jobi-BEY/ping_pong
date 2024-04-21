from pygame import *
from random import choice, randint
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
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500-5-self.rect.h:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__(img,x,y,w,h,speed)
        self.speed_x = 0
        self.speed_y = 0
    def set_direction(self,speed_x,speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
    def upate(self):
        self.rect.x +=self.speed_x*self.speed
        self.rect.y +=self.speed_y*self.speed
    def check_direction(self):
        global score_l, score_r,player_l, player_r, jebspeed, bombom
        if self.rect.y <=5:
            self.speed_y*=-1
        elif self.rect.y>=495-self.rect.height:
            self.speed_y*=-1
        elif self.rect.colliderect(player_l.rect):
            self.speed_x*=-1
            jebspeed-=1
            bombom -= 1
        elif self.rect.colliderect(player_r.rect):
            self.speed_x*=-1
            jebspeed-= 1
            bombom -=1
        elif self.rect.x <=0:
            score_r += 1
            self.rect.x = 350-self.rect.w/2
            self.rect.y = 250-self.rect.h/2
            self.set_direction(choice([-1,1]), choice([-1,1]))
            self.speed = 2
        elif self.rect.x >=700-self.rect.w:
            score_l += 1
            self.rect.x = 350-self.rect.w/2
            self.rect.y = 250-self.rect.h/2
            self.set_direction(choice([-1,1]), choice([-1,1]))
            self.speed = 2
class Bomba():
    def __init__(self,img,x,y,w,h):
        self.image = transform.scale(image.load(img), (w,h))
        self.rect.x = x
        self.rect.y = y
        self.rect.w = w
        self.rect.h = h

font.init()
font1 = font.SysFont('Arial', 36)
direction = [-1,1]
player_l = Player('koral_l.png',10,210,40,100,5)
player_r = Player('koral_r.png',650,210,40,100,5)
ball = Ball('fish_fuga.png',325,225,50,50,2)
window = display.set_mode((700,500))
display.set_caption('saveEcoCity')
FPS = 60
score_l = 0
score_r = 0
jebspeed = 5
bombom = 10
left_win = font1.render('Левый участник выиграл!:)',1,(255,255,255))
right_win = font1.render('Правый участник выиграл!:)',1,(255,255,255))
nexti = 60
finish = True

ball.set_direction(choice(direction), choice(direction))

game = True
clock = time.Clock()
background = transform.scale(image.load('sea.jpg'),(700,500))
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != False:
        window.blit(background,(0,0))
        left_score = font1.render('Счет:'+str(score_l),1,(255,255,255))
        window.blit(left_score,(10,30))
        right_score = font1.render('Счет:'+str(score_r),1,(255,255,255))
        window.blit(right_score,(560,10))
        player_l.reset()
        player_l.move_2()
        player_r.reset()
        player_r.move_1()
        ball.upate()
        ball.check_direction()
        ball.reset()
        if jebspeed < 1:
            ball.speed +=1
            jebspeed = 5
        if bombom == 0:
            bomba = Bomba('unnamed.png',randint(200,500),randint(100,400),50,50)
            bomba.reset()
            
        # if bombom == 0:
        #     bomba = GameSprite('unnamed.png', randint(100))
        if score_l > 4:
            window.blit(left_win,(150,150))
            finish = False
        elif score_r > 4:
            window.blit(right_win,(150,150))
            finish = False

        # for i in range(60):
        #     nexti -= 0.40
        #     for i in range(60):
        #         nexti -= 0.00001
                
        # time_finish = font1.render('До конца игры:'+str(nexti),1,(255,255,255))
        # window.blit(time_finish,(120,10))
        
            
        display.update()
        clock.tick(FPS)