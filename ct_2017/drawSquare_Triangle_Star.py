import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def drawSquareAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for a in range(0,4):
        t1.fd(size)
        t1.rt(90)

def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for a in range(0,3):
        t1.fd(size)
        t1.lt(120)

def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for a in range(0,5):
        t1.fd(size)
        t1.rt(144)

drawSquareAt(-470,0,100)
drawTriangleAt(-100,0,100)
drawStarAt(370,0,100)