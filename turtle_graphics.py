from turtle import *
shelly = Turtle()
for i in range(100):
    for j in range(i):
        shelly.circle(100)
        shelly.left(290)
        shelly.right(90)

shelly.speed(1)
shelly.screen.exitonclick()
