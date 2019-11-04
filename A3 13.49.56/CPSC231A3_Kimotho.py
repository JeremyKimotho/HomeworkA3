import sys
import os
import turtle

WIDTH = 600
HEIGHT = 600
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"

# The function takes in graph points an input and returns the equivalent coordinates on the turtle window. xo,yo are the coordinate points of the graph location 0,0. The ratio is the number of pixels between 0 and 1.
def screenCoor(x, y):
    xo=WIDTH/2
    yo=HEIGHT/2
    ratio=300
    x_coordinate=float(xo+(ratio*x))
    y_coordinate=float(yo+(ratio*y))
    return x_coordinate, y_coordinate

def command_line():
    for arg in sys.argv:
        print(arg)

def read_star_info():
    pass

# Draws only the x-axis. 0,yo is the point halfway up the y-axis and most negative value on x-axis - the graph coordinates are -1,0. The ticks list contains the increments that the axis will go up in.
def drawXAxis(pointer):
    yo=WIDTH/2
    pointer.penup()
    pointer.goto(0,yo)
    pointer.pendown()
    ticks=[-1, - 0.75, - 0.5, - 0.25, 0, 0.25, 0.5, 0.75, 1]
    for i in range(0, len(ticks),1):
        x_value1,y_value1=screenCoor(ticks[i],0)
        pointer.goto(x_value1, y_value1)
        pointer.penup()
        pointer.goto(x_value1, y_value1+3)
        pointer.pendown()
        pointer.goto(x_value1, y_value1-3)
        pointer.goto(x_value1,y_value1)
        pointer.penup()
        pointer.goto(x_value1-5, y_value1-13)
        pointer.pendown()
        if ticks[i]!=0:
            pointer.write(ticks[i])
        pointer.penup()
        pointer.goto(x_value1,y_value1)
        pointer.pendown()

# Draws only the y-axis. xo,0 is the point halfway down the x-axis and most negative value on y-axis - the graph coordinates are 0,-1. The ticks list contains the increments that the axis will go up in.    
def drawYAxis(pointer):
    xo=WIDTH/2
    pointer.penup()
    pointer.goto(xo,0)
    pointer.pendown()
    ticks=[-1, - 0.75, - 0.5, - 0.25, 0, 0.25, 0.5, 0.75, 1]
    for i in range(0, len(ticks),1):
        x_value1,y_value1=screenCoor(0,ticks[i])
        pointer.goto(x_value1, y_value1)
        pointer.penup()
        pointer.goto(x_value1+3, y_value1)
        pointer.pendown()
        pointer.goto(x_value1-3, y_value1)
        pointer.goto(x_value1,y_value1)
        pointer.penup()
        pointer.goto(x_value1+8, y_value1-7)
        pointer.pendown()
        if ticks[i]!=0:
            pointer.write(ticks[i])
        pointer.penup()
        pointer.goto(x_value1,y_value1)
        pointer.pendown()

# Runs the functions that draw the x and y axis
def axis_drawing(pointer):
    drawXAxis(pointer)
    drawYAxis(pointer)

def star_drawing():
    pass

def read_const_info():
    pass

def const_drawing():
    pass

def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.up()
    return pointer

def main():
    command_line()
    #Handle arguments
    #Read star information from file (function)
    pointer = setup()
    #Draw Axes (function)
    pointer.color(AXISCOLOR)
    axis_drawing(pointer)
    #Draw Stars (function)
    #Loop getting filenames
        #Read constellation file (function)
        #Draw Constellation (function)
        #Draw bounding box (Bonus) (function)
    expr = input("Enter an arithmetic expression: ")
    while expr != "":
        expr = input("Enter an arithmetic expression: ")

main()