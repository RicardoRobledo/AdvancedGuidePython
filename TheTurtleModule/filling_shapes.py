'''
Created on 26 dic. 2020

@author: RSSpe
'''

import turtle


def setup():
    """ Provide the config for the screen """
    turtle.title('Filled Square Example')
    turtle.setup(300, 300, 300, 300)
    turtle.hideturtle()

def draw_square(size):
    """ Draw a square in the current direction """
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

setup()

turtle.pencolor('lime')
turtle.fillcolor('skyblue')
turtle.begin_fill()

draw_square(60)

turtle.end_fill()
turtle.done()

# Of course Turtle Graphics is not the only graphics option
# available for Python:

# PyQtGraph
# Pillow
# Pyglet

