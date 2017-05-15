import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle()
turnby=45
size=100
oldpos=t1.pos()
oldhead=t1.heading()
num=1
def wind(size):
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)
    t1.penup()
    t1.setpos(oldpos)
    t1.setheading(oldhead+turnby*num)
    t1.pendown()
for num in range(1,9):
    wind(size)
    num+=1