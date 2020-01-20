import turtle #allows us to use turtles
window = turtle.Screen()   #creates a playground for the turtles
window.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.speed(1)

alex.penup()
size = 20

for _ in range(50):
    alex.stamp()
    size = size + 3
    alex.forward(size)
    alex.left(24)

window.mainloop()
