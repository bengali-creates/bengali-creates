import turtle as t
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def number_of_racer():
    while True:
        try:
            racers=int(input("Enter the number of turtle you want to race from 2 to 10: "))
            if 2<=racers<=10:
                return racers
            else:
                print("Enter the valid number of turtle from 2 to 10: ")
        except ValueError:
            print("Enter a valid number, BITCH!!!!!!")

def create_turtles(colors):
    turtles=[]
    spacing= (WIDTH//(len(colors)+1))
    for i,color in enumerate(colors):
        racer=t.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i*spacing),HEIGHT//2+20)
        racer.pendown
        turtles.append(racer)

    return turtles

def turtel_screen():
    screen = t.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racer=number_of_racer()
turtel_screen()
time.sleep(10)