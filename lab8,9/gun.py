import math
from random import choice
import random

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.t = 0
        
    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if (self.x >= 800 and self.vx > 0 ):
            self.vx = -0.8 * self.vx
        if (self.x <= 0 and self.vx < 0 ):
            self.vx = -0.8 * self.vx
        if (self.y >= 600 and self.vy < 0):
            self.vy = -0.8*self.vy
        if (self.y <= 0 and self.vy > 0):
            self.vy = -0.8*self.vy
            
        self.x += self.vx
        self.y += -1*self.vy 
        self.vy += -1* 2/5
        self.t += 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x-obj.x)**2 + (self.y-obj.y)**2)**(1/2) <= self.r + obj.r:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
             pos = pygame.mouse.get_pos()
             self.an = math.asin((450 - pos[1])/ ((pos[0]-20)**2 + (450-pos[1])**2)**(1/2))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
            

    def draw(self, color):
        if (self.f2_on == 1 and self.f2_power <= 100):
            pos = pygame.mouse.get_pos()
            angle = math.asin((450 - pos[1])/ ((pos[0]-20)**2 + (450-pos[1])**2)**(1/2))
            pygame.draw.line(self.screen, RED, 
                 [20, 450], 
                 [20+self.f2_power*math.cos(angle), 450-self.f2_power*math.sin(angle)],6)
            
            
        else:
            pos = pygame.mouse.get_pos()
            angle = math.asin((450 - pos[1])/ ((pos[0]-20)**2 + (450-pos[1])**2)**(1/2))
            pygame.draw.line(self.screen, GREY, 
                 [20, 450], 
                 [20+10*math.cos(angle), 450-10*math.sin(angle)],6)
        

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__ (self):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.r = random.randint(10,40)
        self.color = GAME_COLORS[random.randint(0,5)]
        self.vx = random.randint(-10,10)
        self.vy = random.randint(-10,10)

    def new_target(self):
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.r = random.randint(10,40)
        self.color = GAME_COLORS[random.randint(0,5)]
        self.live = 1
        self.vx = random.randint(-10,10)
        self.vy = random.randint(-10,10)
        
        
        
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
    def move(self):
        
        if (self.x >= 800 and self.vx > 0 ):
            self.vx = -1*self.vx
        if (self.x <= 0 and self.vx < 0 ):
            self.vx = -1 * self.vx
        if (self.y >= 600 and self.vy < 0):
            self.vy = -1*self.vy
        if (self.y <= 0 and self.vy > 0):
            self.vy = -1*self.vy
            
        self.x += self.vx
        self.y += -1*self.vy 
        
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        

    
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    target1.draw()
    target2.draw()
    target1.move()
    target2.move()
    gun.draw(RED)
    for b in balls:
        if (b.t <=80):
            b.draw()
        else:
            balls.remove(b)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1.new_target()
            balls.remove(b)
        if b.hittest(target2) and target1.live:
            target2.live = 0
            target2.hit()
            target2.new_target()
            balls.remove(b)
    gun.power_up()

pygame.quit()
