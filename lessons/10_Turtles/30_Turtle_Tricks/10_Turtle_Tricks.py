import turtle
turtle.setup(600,600,0,0)
t = turtle.Turtle()


def yin(radius, color1, color2):
    t.width(3)
    t.fillcolor("black")
    t.begin_fill
    t.circle(radius/2., 180)
    t.fillcolor("black")
    t.begin_fill
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius/2., 180)
    t.fillcolor("white")
    t.begin_fill
    t.left(90)
    t.up()
    t.forward(radius*0.375)
    t.right(90)
    t.down()
    t.circle(radius*0.125)
    t.left(90)
    t.end_fill
    t.up()
    t.backward(radius*0.375)
    t.down()
    t.left(90)

def main():
    yin(200, "white", "black")
    yin(200, "black", "white")
    t.ht()
    return "Done!"


"""
Commons: Gingerbrave, Angel, Muscle, Beet, Ninja, Strawberry, Wizard
Rares: Blackberry, Carrot, Clover, Onion, Custard Cookie III, Gumball, Cherry, Devil, Adventurer, Princess, Avocado, Alchemist, Knight
Epics: 
[bomber]
[ambush]
[healer]
[defence]
[charge]
[ranged]
[magic]
'

Super Epics: Doughael, Shining Glitter, Clotted Cream, Stardust, Oyster, Capsaicin, Sherbet, Crimson Coral, 
Specials: Marshmallow Bunny, Snapdragon, Icicle Yeti, Creme Ferret
Legendary: Sea Fairy, Frost Queen, Stormbringer,  Black Pearl, 
"""

main()              
turtle.done()