
#Task 1 - Add Two Numbers

def addNumbers(num1, num2):
    return num1 + num2

answer = addNumbers(15, 25)

print("Answer: ", answer)
print("\n")

#Exercise 1

def add_numbers(num1, num2):
    return num1 + num2

answer = add_numbers(18, 42)

print("Answer: ", answer)
print("\n")

#Exercise 2

def askForNumbers():
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))

    total = x + y
    print("The total is:",total)
    return total

askForNumbers()
print("\n")

#Exercise 3

def askFor3Numbers():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))

    total = a + b + c

    return total

print("Total = ", askFor3Numbers())
print("\n")
