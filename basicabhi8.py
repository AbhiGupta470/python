''' 9. Program to find the hypotenuse of a right angled triangle, when the base and height are entered
by the user.'''
base = float(input("Enter the base"))
height = float(input("Enter the height"))
hypotenuse = (((base*base) + (height*height)) ** 0.5)
print("The hypotenuse is",end=' ')
print(hypotenuse)
