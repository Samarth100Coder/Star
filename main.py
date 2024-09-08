import turtle
turtle.Screen().bgcolor('Red')
t=turtle.Turtle()
t.shape('turtle')
t.color('yellow')
for i in range(3):
    t.forward(200)
    t.left(120)

t.penup()
t.left(90)
t.forward(120)
t.right(90)
t.pendown()
for i in range(3):
    t.forward(200)
    t.right(120)

turtle.done()