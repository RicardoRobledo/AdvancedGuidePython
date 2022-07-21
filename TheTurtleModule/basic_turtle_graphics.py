'''
Created on 26 dic. 2020

@author: RSSpe
'''

# There are in fact two ways of working with the turtle module; one is to use
# the classes available with the library and the other
# is to use a simpler set of functions that hide the classes and objects

import turtle

# set a title for your canvas window
turtle.title('My Turtle Animation')
# set up the screen size (in pixels)
# set the starting point of the turtle (0, 0)
turtle.setup(width=200, height=200, startx=500, starty=300)
# sets the pen color to red
turtle.pencolor('blue')

# Hide cursor
turtle.hideturtle()

# Draw a square
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)

turtle.penup()

# Show cursor
turtle.showturtle()

turtle.backward(50)
turtle.left(90)
turtle.backward(50)
turtle.left(90)
turtle.backward(50)
turtle.left(90)
turtle.backward(50)
turtle.left(90)

turtle.pendown()

turtle.dot(20, 'red')

# …
# Add this so that the window will close when clicked on
turtle.exitonclick()
