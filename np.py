import turtle
import random
turtle.bgcolor('black')
turtle.colormode(255)
x=0
turtle.speed(0)
for x in range(500):
    r,b,g=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    turtle.pencolor(r,g,b)
    turtle.fd(x+30)
    turtle.rt(91)
turtle.exitonclick()