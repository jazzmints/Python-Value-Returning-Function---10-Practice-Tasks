#Task 5 - Calculate Student Average

def averageScore(score1, score2, score3):
    return(score1 + score2 + score3)

average = averageScore(85, 90, 95)

print("Average: ", average)

#Exercise 5.1

def averageNumbers(num1, num2, num3):
    return(num1 + num2 + num3)

average = averageNumbers(80, 90, 100)

print("Average: ", average)
print("\n")

#Exercise 5.2

def subjectAverage():
    math = float(input("Enter Math Score: "))
    science = float(input("Enter Science Score: "))
    english = float(input("Enter English Score: "))
    history = float(input("Enter History Score: "))
    writing = float(input("Enter Writing Score: "))

    subjectAverage = math + science + english + history + writing

    return subjectAverage

print("\nAverage Subject Scores: ", subjectAverage())
print("\n")

#Exercise 5.3

def gradeANDaverage():
    math = float(input("Enter Math Score: "))
    science = float(input("Enter Science Score: "))
    english = float(input("Enter English Score: "))
    history = float(input("Enter History Score: "))
    writing = float(input("Enter Writing Score: "))

    subjectAverage = math + science + english + history + writing
    print("Average: ", subjectAverage)

    if subjectAverage >= 90:
        grade = "A"
    elif subjectAverage >= 80:
        grade = "B"
    elif subjectAverage >= 70:
        grade = "C"
    elif subjectAverage >= 60:
        grade = "D"
    elif subjectAverage < 60:
        grade = "F" 

    print("Grade = ", grade)

    return grade

gradeANDaverage()
