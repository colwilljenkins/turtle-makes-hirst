#import colorgram

# Creating colour list and deleting white
# colours = colorgram.extract('hirst.jpg', 21)
# print(colours)
# rgb_colours = []
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)

rgb_colours = [(213, 169, 105), (248, 251, 250), (78, 92, 124), (199, 240, 245), (252, 235, 236), (122, 166, 204), (137, 168, 154), (122, 97, 85), (187, 134, 149), (252, 237, 57), (89, 70, 77), (216, 64, 78), (88, 118, 101), (155, 128, 79), (168, 201, 191), (96, 131, 163), (221, 100, 81), (223, 173, 180), (227, 174, 167), (91, 136, 162)]
print(rgb_colours)

from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

turt = Turtle()
turt.hideturtle()
turt.penup()
turt.setpos(-200, -200)
for _ in range(10):
    for _ in range(10):
        turt.dot(20, random.choice(rgb_colours))
        turt.forward(50)
    turt.backward(500)
    turt.left(90)
    turt.forward(50)
    turt.right(90)






screen = Screen()
screen.exitonclick()