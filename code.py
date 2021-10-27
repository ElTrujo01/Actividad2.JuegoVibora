# Por:  Jesus A. Trujillo de Anda   A00827538
#       Jorge Avalos                A01720730
#       Carlos Milano               A01383102
#       Carlos Gaeta López          A01611248
#       Alberto Guajardo            A00826548

#Herramientas computacionales: el arte de la programación (Gpo 6)

#Actividad 2. Juego de la Vibora

#ULTIMA FECHA DE MODIFICACION: Miercoles, 27 de octubre de 2021

from turtle import *
from random import randrange
from freegames import square, vector


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

# 2021. Derechos reservados : Ninguna parte de esta obra puede ser reproducida o
# transmitida, mediante ningún sistema o método, electrónico o mecánico, sin conocimiento por escrito 
# de los autores. Tec de Monterrey.