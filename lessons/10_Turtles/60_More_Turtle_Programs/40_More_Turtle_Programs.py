"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location

    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
"""
import turtle as turtle
import random

turtle.setup(width=600, height=600)

t = turtle.Turtle()

t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big
import random

def turtle_clicked(t, x, y):
    """
    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x,y)
    print('turtle clicked!')

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    screen.register_shape(image_path)
    turtle.shape(image_path)

# Set up the screen

# Connect the turtle to the turtle_clicked function
set_turtle_image(t,"pikachu.gif")
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
