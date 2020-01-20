numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0,]

#mark = int(input("please input the exam mark to get the grade: "))
#the abive statement is commented out cos we want check the numbers list above instead


"""
Program asks for the exam mark and prints the mark's grade
"""

message = "" #create a msg variable

for number in numbers:
    mark = float(number)
    if mark >= 75:
        print(message + str(mark) + " is 'First' Grade")
    elif mark in range(70, 75):
        print(message + str(mark) + " is 'Upper Second' Grade")
    elif mark in range(60, 70):
        print(message + str(mark) + " is 'Second' Grade")
    elif mark in range(50, 60):
        print(message + str(mark) + " is 'Third' Grade")
    elif mark in range(45, 50):
        print(message + str(mark) + " is 'F1 Supp' Grade")
    elif mark in range(40,45):
        print(message + str(mark) + " is 'F2' Grade")
    else:
        print(message + str(mark) + " is 'F3' Grade")
    


