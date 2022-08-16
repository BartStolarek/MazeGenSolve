# A Simple Maze Game Tutorial by @TokyoEdTech
# Python 2 and Python 3 Compatible
# Part 1: Setting Up The Maze
import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)

#Create Pen

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Create levels list
levels = [""]

#Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X        X        X           XX",
    "X        X        X           XX",
    "X  XXXX  X  XXXX  X  XXXXXXX  XX",
    "X  X     X     X     X  X     XX",
    "X  X     X     X     X  X     XX",
    "X  XXXXXXXXXX  XXXX  X  X  XXXXX",
    "X     X     X     X     X  X  XX",
    "X     X     X     X     X  X  XX",
    "XXXX  X  XXXX     XXXXXXX  X  XX",
    "X        X     X     X        XX",
    "X        X     X     X        XX",
    "X  XXXXXXX     XXXXXXX  XXXXXXXX",
    "X           X     X           XX",
    "X           X     X           XX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXX    XX"

]

level_2 = [
    "XOOOXOOOXOOOOX",
    ""


]

#Add Maze to mazes list
levels.append(level_1)

#Create level setup function

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            #NOTE the order of y and x int he next line
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -450 + ( x * 30)
            screen_y = 128 - (y*16)

            #Check if it is an X (representing a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

#Create class isntances
pen = Pen()

#Set up the level
setup_maze(levels[1])

while True:
    pass