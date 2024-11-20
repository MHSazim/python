from turtle import *
import colorsys

bgcolor('black')
tracer(500)

def draw():
    h = 0
    for i in range(90):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Generate color using HSV
        h += 0.01  # Small increment for smoother color change
        up()
        goto(0, 0)  # Go to the center
        down()
        color('black')  # Outline color
        fillcolor(c)  # Fill color
        begin_fill()
        rt(98)  # Rotate
        circle(i, 12)  # Draw circle based on `i`
        fd(290)  # Move forward
        fd(i)  # Move forward based on `i`
        lt(290)  # Rotate left
        for j in range(129):  # Loop for additional drawing
            fd(i)
            circle(j, 299, steps=2)  # Draw a polygon-like shape
        end_fill()  # End filling the shape

draw()  # Call the draw function
done()