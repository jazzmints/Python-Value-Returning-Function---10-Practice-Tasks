#Task 3 - Find Area of a Rectangle

def rectangleArea(length, width):
    return length * width

area = rectangleArea(12, 5)

print("Area: ", area)
print("\n")

#Exercise 1

def area(length, width):
    return length * width

area = rectangleArea(9, 6)

print("Area: ", area)
print("\n")

#Exercise 2

def rectangleDimensions():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))

    return length * width

print("The rectangle area is ", rectangleDimensions(), "square units.")
print("\n")

#Exercise 3 

def calc3Rectangles():
    print("For the First Rectangle: ")
    length1 = float(input("Enter the length of the 1st rectangle: "))
    width1 = float(input("Enter the width of the 1st rectangle: "))

    rectangle1 = length1 * width1

    print("\n")
    print("For the Second Rectangle: ")
    length2 = float(input("Enter the length of the 2nd rectangle: "))
    width2 = float(input("Enter the width of the 2nd rectangle: "))

    rectangle2 = length2 * width2

    print("\n")
    print("For the Third Rectangle: ")
    length3 = float(input("Enter the length of the 3rd rectangle: "))
    width3 = float(input("Enter the width of the 3rd rectangle: "))

    rectangle3 = length3 * width3

    totalArea = rectangle1 + rectangle2 + rectangle3

    print("\n")
    print("Rectangle 1 Area = ", rectangle1)
    print("Rectangle 2 Area = ", rectangle2)
    print("Rectangle 3 Area = ", rectangle3)
    print("Total Area = ", totalArea)

calc3Rectangles()
