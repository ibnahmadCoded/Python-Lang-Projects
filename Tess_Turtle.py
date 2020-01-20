import turtle #allows us to use turtles
window = turtle.Screen()   #creates a playground for the turtles
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

tess.penup()
size = 100


tess.stamp()

for _ in range(12):
    tess.forward(60)
    tess.pendown()
    tess.forward(30)
    tess.penup()
    tess.forward(10)
    tess.stamp()
    tess.forward(-100)
    tess.left(30)

