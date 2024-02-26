def main():
    move(5,1,3)
def move (disks, fromPeg, toPeg):
    if disks > 0:
        other = 6 - fromPeg - toPeg
        move(disks-1, fromPeg, other)
        print("Move disk form peg", fromPeg, "to", toPeg)
        move(disks-1, other, toPeg)
main()  
'''shelly.penup()
shelly.left(45)
shelly.forward(100)
shelly.pendown()
for i in range(4):
    shelly.forward(100)
    shelly.left(90) '''