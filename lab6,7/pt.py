import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

number_of_circles = 10
number_of_squares = 5
'''переменные, отвечающие за количество кружков и квадратов'''

points = 0
'''переменная, отвечающая за количество очков'''

print('write your name')
name = str(input())

new = True

file = open('score.txt', 'r')

lines = file.readlines()
lenght = len(lines)
tmp2 = lenght//2
'''считываем все строки'''

best_point = 0

# итерация по строкам
for i in range (0,lenght,1):
    if (lines[i].strip() == name):
        best_point = int(lines[i+1])
        new = False

players = {lines[2*i].strip(): int(lines[2*i+1]) for i in range (0,tmp2,1)}
print("Текущий список лидеров")
print(players)

file.close

f = open('score.txt', 'w')

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
'''Вводится массив из цветов'''

x_circle = []
y_circle = []
dx_circle = []
dy_circle = []
r_circle = []
color_circle = []

x_square =[]
y_square = []
dx_square = []
dy_square = []
l_square = []
color_square = []
'''Два блока массивов, которые отвечают за координаты, скорости, цвета и размеры
объектов'''

for i in range (0,number_of_squares,1):
    x_square.append(randint(300,500))
    y_square.append(randint(300,500))
    dx_square.append(randint(-10,10))
    dy_square.append(randint(-10,10))
    l_square.append(randint(20,30))
    color_square.append (COLORS[randint(0, 5)])

for i in range (0,number_of_circles,1):
    x_circle.append(randint(300,500))
    y_circle.append(randint(300,500))
    r_circle.append(randint(20,40))
    dx_circle.append(randint(-10,10))
    dy_circle.append(randint(-10,10))
    color_circle.append (COLORS[randint(0, 5)])
'''Два блока массивов заполняются рандомными цветами, координиатами, скоростями
и размерами объектов'''
    
FPS = 60
'''Кадры в секунду'''

screen = pygame.display.set_mode((1200, 800))
'''Окно pygame'''

def new_ball(x,y,r,color):
    circle(screen, color, (x, y), r)
'''Функция для отрисовки шара на экране'''

def figure_goto(x,y,dx,dy):
    x = x+dx
    y = y+dy
    return(x,y)
'''Функция, которая перемщает фигуру по экрану'''

def new_square(x,y,l,color):
    rect(screen, color, (x,y,l,l))
'''Функция для отрисовки квадрата на экране'''

    
pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            '''Отслеживание нажатия мыши'''
            for i in range (0, number_of_circles,1):
                if ( (event.pos[0] - x_circle[i])**2 +
                     (event.pos[1] - y_circle[i])**2 <= r_circle[i]**2 ):
                    x_circle[i] = randint (300,500)
                    y_circle[i] = randint(300,500)
                    dx_circle[i] = randint (-10,10)
                    dy_circle[i] = randint (-10,10)
                    points += 1
                    print(points)
                    '''Шар пропадает, отрисовывается в другом месте и
                        прибавляются очки'''
                    
            for i in range (0, number_of_squares,1):
                if (event.pos[0] >= x_square[i] and event.pos[0] <= x_square[i] + l_square[i] and
                    event.pos[1] >= y_square[i] and event.pos[1] <= y_square[i] + l_square[i]):
                    x_square[i] = randint(300,500)
                    y_square[i] = randint(300,500)
                    dx_square[i] = randint(-10,10)
                    dy_square[i] = randint(-10,10)
                    points+= 5
                    print(points)
                    '''Квадрат пропадает, отрисовывается в другом месте и
                        прибавляются очки'''

            
    for i in range (0,number_of_circles,1):
        new_ball(x_circle[i],y_circle[i],r_circle[i],color_circle[i])
        x_circle[i], y_circle[i] = figure_goto(x_circle[i],y_circle[i],
                                               dx_circle[i],dy_circle[i])
        '''Отрисовывается шар и перемещается вперед'''
        
        if ( x_circle[i] - r_circle[i] <= 0):
            
            dx_circle[i] = randint(1,20)
            dy_circle[i] = randint(-20,20)
            
        if ( x_circle[i] + r_circle[i] >= 1200):
            dx_circle[i] = randint(-10,-1)
            dy_circle[i] = randint(-10,10)
                
        if ( y_circle[i] - r_circle[i] <= 0):
            
            dy_circle[i] = randint(1,10)

        if ( y_circle[i] + r_circle[i] >= 800 ):

            dy_circle[i] = randint (-10,-1)
        '''Условия на столкновение с границей экрана - скорость меняется на
            случайную в противоположном направлении'''
                
    for i in range (0,number_of_squares,1):
        
        new_square(x_square[i],y_square[i],l_square[i],color_square[i])
        x_square[i], y_square[i] = figure_goto(x_square[i],y_square[i],
                                               dx_square[i],dy_square[i])
        '''Квадрат отрисовывается и перемещается'''
        
        if (x_square[i] <= 0): 
            
            dx_square[i] = randint(1,10)
            
        if (x_square[i] + l_square[i] >= 1200):
            dx_square[i] = randint(-10,-1)
        if (y_square[i] <= 0):
            
            dy_square[i] = randint(1,10)

        if (y_square[i] + l_square[i] >= 800):

            dy_square[i] = randint(-10,-1)
        '''Условие на столкновение с границей экрана - скорость меняется на
            случайную в противоположном направлении'''
        
    points_string = str(points)
    '''Переводим очки в строку чтобы вывести на экран'''
    
    f2 = pygame.font.SysFont('serif', 48)
    text2 = f2.render(points_string, False,
                  (0, 180, 0))   
    screen.blit(text2, (10, 10))
    '''Выводим на экран очки'''
    
    pygame.display.update()
    screen.fill(BLACK)
    
if ( new == True ):
    players[name.strip()] = points
else:
    if (players[name.strip()] <= points):
        players[name.strip()] = points

'''Проверяем, у нас играет новый игрок или игрок из уже существующего
списка лидеров'''
    
pygame.quit()
'''Конец цикла pygame'''

top_players = dict(sorted(players.items(), key = lambda val: val[1]))
print(top_players)
'''Записываем игроков в словарь и фильтруем'''

for i in top_players:
    f.write(str(i) + '\n')
    f.write(str(top_players[i]) + '\n' )
f.close()
'''Записываем результат в файл'''
