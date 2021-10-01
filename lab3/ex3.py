import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1500, 800))
tmp = pygame.display.set_mode((1500, 800))
black = (0,0,0)
blue = (0, 255,255)
green =(154,205,50)
white = (255,255,255)
brown =(139,69,19)
red = (255,0,0)
grey = (216, 191, 216)
lavender = (230,230,250)
yellow = (255, 215, 0)
pink = ( 212, 15, 252)

def icecream():
    polygon(screen, yellow, [[280, 490], [280, 400], [190, 430]])
    circle(screen, red, (260, 390), 30)
    circle(screen, brown, (215, 410), 30)
    circle(screen, white, (230, 380), 30)

def background():
    rect(screen, blue, (0, 0, 1500, 400))
    rect(screen, green, (0, 400, 1500, 400))

def man():

    ellipse(screen, grey, (400, 280, 170, 400))
    circle(screen, lavender, (485, 245), 70)

    aalines(screen, black, False, [[500, 650], [530, 750],  [570, 760]])
    aalines(screen, black, False, [[450, 630], [430, 770],  [400, 780]])
    line(screen, black,  [270, 490], [440, 330], 1)
    line(screen, black,  [700, 490], [540, 330], 1)

def woman ():
    line(screen, black,  [700, 490], [900, 330], 1)
    polygon(screen, pink, [[900, 320], [1000, 630], [800, 630]])
    circle(screen, white, (900, 270), 70)
    aalines(screen, black, False, [[850, 600], [850, 700],  [800, 700]])
    aalines(screen, black, False, [[950, 600], [950, 700],  [1000, 700]])
    aalines(screen, black, False, [[905, 350], [960, 400],  [1050, 350]])

def baloon ():
    line(screen, black,  [1050, 400], [1060, 250], 1)
    polygon(screen, red, [[1060, 250], [1100, 200], [1020, 190]])
    circle(screen, red, (1045, 195), 25)
    circle(screen, red, (1080, 195), 25)

def all():
    background()
    man()
    woman()
    baloon()
    icecream()

all()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
