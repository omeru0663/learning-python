import turtle 
pen = turtle.Turtle()
pen.speed(4)
def drawrectangle(size):
    for i in range(2):
        pen.forward(size*2)
        pen.left(90)
        pen.forward(size)
        pen.left(90)
def drawverticalrectangle(size):
     for i in range(2):
        pen.forward(size)
        pen.left(90)
        pen.forward(size*2)
        pen.left(90)
def drawtriangle(size):
     pen.penup()
     pen.setpos(0,200)
     pen.pendown()
     pen.left(30)
     pen.forward(size)
     pen.right(60)
     pen.forward(size)

windowy = [150,150,50,50]
windowx = [50,250,50,250]
drawrectangle(200)
pen.forward(150)
drawverticalrectangle(50)
for i in range(4):
    pen.penup()
    pen.setpos(windowx[i],windowy[i])
    pen.pendown()
    drawrectangle(25)
    pen.penup()
    pen.pendown()
drawtriangle(234)


