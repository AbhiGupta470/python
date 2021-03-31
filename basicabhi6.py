'''7. Program to find the area and perimeter of a rectangle, when the required input (Length and
Breadth) are entered by the user.'''
Length= float(input("Enter the length"))
Breadth = float(input("Enter the breadth"))
area = Length* Breadth
print("The area is",end=' ')
print(area)
perimeter = 2*(Length + Breadth)
print("The perimeter is",end=' ')
print(perimeter)
