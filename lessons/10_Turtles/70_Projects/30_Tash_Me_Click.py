# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here ) to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
# Your code here
import random

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.register_shape(image_path)
    turtle.shape(image_path)

def turtle_clicked(t, x, y):
    """
    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """
    
    
    t.goto(x,y)
    print('turtle clicked!')
import turtle
turtle.setup(width=300, height=300)

t = turtle.Turtle()

screen = turtle.Screen()
t.goto(0,-50)

set_background_image(screen, "emoji.png")
set_turtle_image(t, "moustache2.gif")
turtle.onscreenclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done()