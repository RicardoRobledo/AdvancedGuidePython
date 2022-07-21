'''
Created on 31 dic. 2020

@author: RSSpe
'''

import turtle


def setup_screen(title="Fractal Tree", background='white', screen_size_x=990, screen_size_y=650):
    print('Set up Screen')
    turtle.title(title)
    turtle.setup(screen_size_x, screen_size_y, 180, 30)
    #turtle.hideturtle()
    turtle.speed(1000)
    turtle.penup()
    turtle.backward(50)
    turtle.bgcolor(background)
    turtle.setposition(0, -290)

def draw(branches, distancia):
    
    if not branches==0:
        
        distancia*=0.8
        
        turtle.left(30)

        turtle.forward(distancia)
        
        draw(branches-1, distancia)
        
        turtle.backward(distancia)
        turtle.right(60)
        turtle.forward(distancia)
        
        draw(branches-1, distancia)
        
        turtle.backward(distancia)
        turtle.left(30)


setup_screen()

distancia = 120
branches = 15

turtle.color('BLUE')
turtle.left(90)
turtle.pendown()
turtle.forward(distancia)

draw(branches, distancia)

turtle.update()
print('Done')
turtle.done()
