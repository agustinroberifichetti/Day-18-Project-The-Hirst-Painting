# ###The following commented code does not work in repl.it as there is no access to the colorgram package here, but I left it there to show the origin of the "colors_list" list.###

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
#
# ###I copied the rgb_colors list result of the "print(rgb_colors)" statement from the console and I pasted it in the code of this file and gave it the name "colors_list".###

import turtle as t
import random as rd

t.colormode(255)

colors_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
               (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
               (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
               (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
               (176, 192, 208), (168, 99, 102)]

timmy = t.Turtle()
screen = t.Screen()

timmy.penup()
timmy.hideturtle()
timmy.speed(0)

for n in range(0, 501, 50):
    timmy.goto(-250, -250 + n)
    for _ in range(10):
        timmy.dot(20, rd.choice(colors_list))
        timmy.forward(50)

screen.exitonclick()
