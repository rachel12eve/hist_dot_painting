import colorgram
from turtle import Turtle, Screen
import random

# color_theme=[]
# Extract 6 colors from an image.
# no_of_color=30
# colors = colorgram.extract('dot_image.jpg', no_of_color)
# print(colors[0].rgb[1])
# print(colors)

# for color in colors:
#     r=color.rgb.r#(colors[color_range].rgb[0])
#     g=color.rgb.g#(colors[color_range].rgb[1])
#     b=color.rgb.b#(colors[color_range].rgb[2])
#     rgb=(r,g,b)
#     color_theme.append(rgb)
# print(color_theme)
screen = Screen()
screen.colormode(255)
color_list = [(240, 244, 249), (117, 98, 76), (63, 92, 143), (128, 163, 193), (192, 144, 164), (67, 44, 33),
              (53, 119, 76), (217, 205, 112), (162, 159, 57), (122, 73, 93), (225, 83, 69), (129, 179, 158),
              (201, 84, 106), (226, 169, 186), (78, 116, 197), (59, 42, 54), (73, 167, 101), (54, 54, 102),
              (44, 46, 66), (53, 170, 187), (85, 50, 71), (30, 85, 57), (227, 175, 165), (88, 55, 46), (41, 58, 48),
              (219, 219, 16)]
turtle = Turtle()
color = random.choice(color_list)
turtle.speed("fastest")
turtle.pu()
turtle.setpos(-300, -300) #move the starting point to left hand corner
turtle.hideturtle()


def move_up_left():
    """have the turtle move up and go back to the left hand corner"""
    #turtle.dot(20,color)
    turtle.setheading(90)
    turtle.fd(50)
    turtle.setheading(180)
    turtle.fd(500)
    turtle.setheading(0)


def forward():
    """have the turtle takes 10 steps"""
    turtle.dot(20, random.choice(color_list))
    turtle.fd(50)


for _ in range(0, 10):
    for _ in range(0, 10):
        forward()
    move_up_left()


screen.exitonclick()
