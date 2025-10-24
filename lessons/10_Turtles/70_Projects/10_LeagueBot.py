""" 
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 
"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')


t = turtle.Turtle
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.register_shape(image_path)
    turtle.shape(image_path)

set_turtle_image(t,"leaguebot_bolt.gif")
turtle.pencolor('blue') 

def draw_polygon(sides,length):
    angle = 360/sides

    for i in range(sides):
        t.forward(length)
        t.left(angle)

draw_polygon(6, 50)
turtle.done()