import turtle #allows us to use turtles
window = turtle.Screen()   #creates a playground for the turtles
window.bgcolor("lightgreen")
alex = turtle.Turtle()   #Creates a Turtle, names it alex

alex.forward(50)      #tell alex to move forward by 50 units
alex.left(90)           #tell alex to turn 90 degrees
alex.forward(30)        #complete the other side of the rectangle

window.mainloop()       #wait for user to close window
