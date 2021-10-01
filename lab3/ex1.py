import pygame
from pygame.draw import *


    
FPS = 30
screen = pygame.display.set_mode((800, 800))
color = (230, 230, 250)

rect(screen, color, (0, 0, 800, 800), 800)
circle(screen, (0, 0, 0), (400, 400), 202)
circle(screen, (255, 215, 0), (400, 400), 200)

circle(screen, (0, 0, 0), (320, 340), 40)
circle(screen, (255, 69, 0), (320, 340), 38)
circle(screen, (0, 0, 0), (320, 340), 20)

circle(screen, (0, 0, 0), (500, 340), 35)
circle(screen, (255, 69, 0), (500, 340), 33)
circle(screen, (0, 0, 0), (500, 340), 15)
polygon(screen, (0, 0, 0), [(380,340), (280,250),(280,230),(380,320)])
polygon(screen, (0, 0, 0), [(450,340), (550,240), (550,220), (450,320)])
rect(screen, (0,0,0), (300, 450, 200, 50))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
