"""
This program calculates the hypotenaus of a right angled triangle
given the lenghts of the other two sides
"""

message = ""

first_side = eval(input("What is the length of the first side?\n"))
second_side = eval(input("What is the length of the second side?\n"))

hypotenaus = ((first_side**2) + (second_side**2))**0.5

print("the First side is: ", first_side)
print("the Second side is: ", second_side)
print("The Hypotenaus is: ", hypotenaus)
