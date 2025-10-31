import random
import turtle

t = turtle.Turtle() # Create a turtle named t
turtle.setup(600,600,0,0)
window = turtle.Screen()
t.speed(10)

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

for i in range(360):
    t.pendown
    t.pencolor(getRandomColor())
    t.fillcolor(getRandomColor())
    t.left(67 + i)
    t.forward(80)
    t.right(250 + i)
    t.forward(80)

#def make_a_shape(t):
    

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

#num_shapes = ...

#for i in range(...):
    #make_a_shape(t)
    #t.right(360/num_shapes)
turtle.done()    