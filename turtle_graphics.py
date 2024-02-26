'''from turtle import *
shelly=Turtle()
for i in range(100):
    for j in range(i):
        shelly.circle(100)
        shelly.left(290)
        shelly.right(90)

shelly.speed(10)
shelly.screen.exitonclick()
'''
from turtle import *

shelly = Turtle()
shelly.speed(0)
class Chess:
    def init_chess_board(self,n,d,c1,c2):
        self.n=n
        self.d=d
        self.c1=c1
        self.c2=c2
        self.draw_square()
    def draw_square():
        for i in range(4):
            shelly.forward(100)
            shelly.right(90)
shelly.screen.exitonclick()