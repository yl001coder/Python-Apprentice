"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 



colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors
   print(color)
   turtle.pencolor(color)
   turtle.left(90)
   turtle.forward(100)


# 2) Make another square, but put the colors in reverse order, using a negative index. 
turtle.penup
turtle.forward(150)
turtle.pendown

for color in colors:
   print(color)
   turtle.pencolor(color)
   turtle.left(90)
   turtle.forward(100)

turtle.done()                     # Close the window when we click on it