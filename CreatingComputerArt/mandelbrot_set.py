'''
Created on 31 dic. 2020

@author: RSSpe
'''

import turtle


for y in range(IMAGE_SIZE_Y):
    zy = y * (MAX_Y - MIN_Y) / (IMAGE_SIZE_Y - 1) + MIN_Y
    for x in range(IMAGE_SIZE_X):
        zx = x * (MAX_X - MIN_X) / (IMAGE_SIZE_Y - 1) + MIN_X
        z = zx + zy * 1j
        c = z
        for i in range(MAX_ITERATIONS):
            if abs(z) > 2.0:
                break
            z = z * z + c
turtle.color((i % 4 * 64, i % 8 * 32, i % 16 * 16))
turtle.setposition(x - SCREEN_OFFSET_X,
                   y - SCREEN_OFFSET_Y)

turtle.pendown()
turtle.dot(1)
turtle.penup()

turtle.done()

