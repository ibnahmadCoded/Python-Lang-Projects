import turtle

def draw_multicolor_square(animal, size):
    """
Make an animal draw a multicolor square of a given size
"""
    colors = ["red", "purple", "hotpink", "blue"]
    for color in colors:
        animal.color(color)
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()    #set up window and its attributes
window.bgcolor("lightgreen")
window.title("Multicolor Squares by Tess")


tess = turtle.Turtle()      #set up tess and some attributes
tess.pensize(3) 


size = 20                   #size of the smallest square

for _ in range(15):
    draw_multicolor_square(tess, size)
    size += 10              #Increase size for each new square
    tess.forward(10)        #move tess forward a little
    tess.right(18)          #give tess some turn

window.mainloop()           #wait for window to be closed
