"""
a program which, given the length of three sides of a triangle,
will determine whether the triangle is rightangled. Assuming that
the third side is the logest side
"""

first_side = eval(input("What is the length of the first side?\n"))
second_side = eval(input("What is the length of the second side?\n"))
third_side = eval(input("What is the length of the longest side?\n"))

threshold = 1e-1   #for checking appoximate floating point numbers (precision)

#calculate hypotenause depending on the sizes of the sides

if third_side > first_side and third_side > second_side:
    hypotenaus = ((first_side**2) + (second_side**2))**0.5
    perimeter = first_side + second_side + third_side
    if abs(hypotenaus - third_side) < threshold: #check against threshold
        print("The triangle with sides ", first_side, second_side, third_side,
          " is rightangled with a perimeter of ", perimeter)
    else:
        print("The triangle with sides ", first_side, second_side, third_side,
          " is not rightangled but has a perimeter of ", perimeter)

if second_side > first_side and second_side > third_side:
    hypotenaus = ((first_side**2) + (third_side**2))**0.5
    perimeter = first_side + second_side + third_side
    if abs(hypotenaus - second_side) < threshold:   #check against threshold
        print("The triangle with sides ", first_side, second_side, third_side,
          " is rightangled with a perimeter of ", perimeter)
    else:
        print("The triangle with sides ", first_side, second_side, third_side,
          " is not rightangled but has a perimeter of ", perimeter)

if first_side > third_side and first_side > second_side:
    hypotenaus = ((third_side**2) + (second_side**2))**0.5
    perimeter = first_side + second_side + third_side
    if abs(hypotenaus - first_side) < threshold:  #check against threshold
        print("The triangle with sides ", first_side, second_side, third_side,
          " is rightangled with a perimeter of ", perimeter)
    else:
        print("The triangle with sides ", first_side, second_side, third_side,
          " is not rightangled but has a perimeter of ", perimeter)
        
if first_side == third_side and third_side == second_side:
    perimeter = first_side + second_side + third_side
    print("The triangle with sides ", first_side, second_side, third_side,
          " is not rightangled, but an equalateral triangle with a perimeter of ", perimeter)


