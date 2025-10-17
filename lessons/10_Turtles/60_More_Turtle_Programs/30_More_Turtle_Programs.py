"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
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

# Set up the screen
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji.png") # Set the background image of the screen
set_turtle_image(tina, "girl_blue.gif")

turtle.exitonclick()      