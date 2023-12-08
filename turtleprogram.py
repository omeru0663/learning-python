import turtle
def draw_square(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(45)
def draw_star(t,sz):
    for i in range(5):
        t.forward(sz)
        t.left(144)
def draw_generalstar(t,sz,rev=2, points=5):
   for i in range(points):
    t.forward(sz)
    t.right(360/points*rev)
wn=turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
draw_generalstar(alex,30,1,20)
# Create a new turtle and set its speed to the fastest possible




colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
