''' 8. Program to find the area and circumference of a circle, when the radius is entered by the user.
However, the user can input radius in integer or float.'''
radius = float(input("Enter the radius"))
area = 3.14 * radius * radius
print("The area is",end=' ')
print(area)
circumference = 2 * 3.14 * radius  
print("The circumference is",end=' ')
print(circumference)
