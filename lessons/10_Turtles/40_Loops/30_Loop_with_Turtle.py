"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

import turtle
turtle.setup(600,600,0,0) # Your code here

tina = turtle.Turtle()

tina.shape('turtle')
tina.speed(2)
tina.pendown

for i in range(5):
    tina.forward(100)
    tina.left(72)

turtle.exitonclick 
