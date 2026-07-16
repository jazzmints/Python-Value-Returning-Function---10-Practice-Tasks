#Task 9

def simpleInterest(principal, rate, time):
    return (principal * rate * time) / 100

interest = simpleInterest(5000, 6, 3)

print("Interest: ", interest)


#Exercise 1

def interest(principal, rate, time):
    return(principal * rate * time) / 100

theInterest = interest(4000, 5, 4)

print("Principal = 4000")
print("Rate = 5%")
print("Time = 4 years")
print("Interest =", theInterest)
print("\n")

#Exercise 2

def askUser():
    principal = float(input("Enter Principal: $"))
    rate = float(input("Enter Rate: %"))
    time = float(input("Enter Years: "))

    print("\n")

    interest = (principal * rate * time) / 100

    print("Interest: $", interest)

    return interest 
askUser()
print("\n")

#Exercise 3

def finalAmount():
    principal = float(input("Enter Principal: $"))
    rate = float(input("Enter Rate: %"))
    time = float(input("Enter Years: "))

    print("\n")

    interest = (principal * rate * time) / 100
    finalAmount = principal + interest

    print("Interest: $", interest)
    print("Final Amount: $", finalAmount)

    return interest and finalAmount
finalAmount()
