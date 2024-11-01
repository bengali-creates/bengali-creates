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

def race(colors):
    turtles=create_turtles(colors)
    while True:
        for racer in turtles:
            move=random.randrange(1,20)
            racer.forward(move)

            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles=[]
    spacing= (WIDTH//(len(colors)+1))
    for i,color in enumerate(colors,start=1):
        racer=t.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i*spacing),-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def bet(colors):
    print("The turtle participating are : ")
    for i,turtle in enumerate(colors, start=1):
        print(i,".",turtle)
    while True:
        try:
            bet=int(input("Enter the number of turtle you want to bet :"))
            if 2<=bet<=len(colors):
                return bet
            else:
                print(f"Enter the valid number of turtle from 2 to {len(colors)}: ")
        except ValueError:
            print("Enter a valid number, BITCH!!!!!!")

def turtel_screen():
    screen = t.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racer=number_of_racer()
turtel_screen()

random.shuffle(COLORS)
colors=COLORS[:racer]
bet(colors)

winner=race(colors)
if (colors[bet]==winner):
    print("You won the bet")
print("The winner is: ",winner)
time.sleep(5)