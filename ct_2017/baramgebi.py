import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def giyuk(size):
  t1.fd(size)
  t1.rt(90)
  t1.fd(size)
t1.home()
t1.clear()
turnby=45
size=100
oldpos=t1.pos()
oldhead=t1.heading()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
t1.setheading(oldhead+turnby)
t1.pendown()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
t1.setheading(oldhead+turnby*2)
t1.pendown()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
t1.setheading(oldhead+turnby*3)
t1.pendown()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
t1.setheading(oldhead+turnby*4)
t1.pendown()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
t1.setheading(oldhead+turnby*5)
t1.pendown()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
t1.setheading(oldhead+turnby*6)
t1.pendown()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
t1.setheading(oldhead+turnby*7)
t1.pendown()
giyuk(size)
t1.penup()
t1.setpos(oldpos)
