lengthInput = int(input("Input field length in feet: "))
widthInput = int(input("Input field width in feet: "))
costInput = int(input("Input cost per ft^2: "))

perimiter = (lengthInput * 2) + (widthInput * 2)
area = lengthInput * widthInput
costTotal = area * costInput

print("The cost of a field with an area of {}ft^2 and a perimiter of {}ft will be ${}".format(area, perimiter, costTotal))