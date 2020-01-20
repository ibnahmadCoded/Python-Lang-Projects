import turtle #allows us to use turtles
window = turtle.Screen()   #creates a playground for the turtles
window.bgcolor("lightgreen")
window.title("Tess and Alex")

tess = turtle.Turtle()   #create Tess
tess.color("red")

alex = turtle.Turtle()   #Create a Turtle, name it alex
alex.color("blue")

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)

alex.forward(80)      #tell alex to move forward by 50 units
alex.left(90)           #tell alex to turn 90 degrees
alex.forward(80)        #complete the other side of the rectangle
alex.left(90)
alex.forward(80)
alex.left(90)
alex.forward(80)
alex.right(90)
alex.forward(100)
alex.right(90)
alex.forward(30)
alex.right(90)
alex.forward(100)

tess.right(150)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(70)
tess.left(125)
tess.forward(120)
tess.right(35)
tess.forward(80)
tess.right(90)
tess.forward(20)


window.mainloop()       #wait for user to close window
