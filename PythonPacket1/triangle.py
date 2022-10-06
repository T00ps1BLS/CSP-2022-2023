from math import sqrt


side1 = int(input("Input first side length (must be less than 5): "))
side2 = int(input("Input second side length (cannot be larger than 5): "))

if side1 >= 5:
    side1 = input("Input must be less than 5: ")
elif side2 >= 5:
    side2 = input("Input must be less than 5: ")

if side1 >= side2:
    side3 = side1 - side2
elif side2 >= side1:
    side3 = side2 - side1

s = (side1 + side2 + side3)
area = sqrt(s*(s - side1)*(s - side2)*(s - side3))

print("Your triange will be a {}ft, {}ft, {}ft triangle with an area of {}".format(side1, side2, side3, area))