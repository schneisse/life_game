import pygame as p
from pygame.locals import *
# Константы цветов RGB

BLACK = (0 , 0 , 0)

RED   = (255 , 0 , 0)

VIOLET= (255 , 0 , 255)

WHITE = (255 , 255 , 255)

YELLOW = (0 , 127 , 255)

# Создаем окно

root = p.display.set_mode((1000 , 500))

#print( root.get_height() )

#print( root.get_width() )

# Основной цикл

while 1:

    # Заполняем экран белым цветом

    root.fill(WHITE)

    # Рисуем сетку

    for i in range(0 , root.get_height() // 20):

       p.draw.line(root , BLACK , (0 , i*(root.get_height()//20) ) , (root.get_width() - i*( root.get_width() // 20), root.get_height()))

    for i in range(0 , root.get_height() // 20):

       p.draw.line(root , BLACK , (i*(root.get_height()//20) , 0 ) , (root.get_height(), root.get_width() - i*( root.get_width() // 20)))


    for j in range(0 , root.get_width() // 20):

        p.draw.line(root , BLACK , (j * 20 , 0) , (j * 20 , root.get_height()))

    # Нужно чтобы виндовс не думал что программа "не отвечает"

    while 1:
        for i in p.event.get():

            if i.type==	QUIT:

                quit()

        p.display.update()

