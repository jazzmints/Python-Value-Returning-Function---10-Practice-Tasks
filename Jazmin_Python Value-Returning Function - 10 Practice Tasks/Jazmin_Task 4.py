#Task 4 - Calculate Employee Weekly Pay

def weeklyPay(hours, rate):
    return hours * rate

pay = weeklyPay(40, 22)

print("\n")
print("Weekly Pay: $", pay)

#Exercise 1

def weeklyPay(hours, rate):
    return hours * rate

pay = weeklyPay(40, 22)

print("\n")
print("Weekly Pay: $", pay)

#Exercise 2

def employeePay():
    employee = input("Enter Employee Name: ")
    hours = float(input("Enter Hours Worked: "))
    hourlyRate = float(input("Enter Hourly Rate: "))

    weeklyPay = hours * hourlyRate

    print("\n")
    print("Employee: ", employee)
    print("Weekly Pay = $", weeklyPay)

    return weeklyPay

employeePay()

#Exercise 3 

def grandPayroll():
    employeeA = input("Enter Employee A Name: ")
    hoursA = float(input("Enter Hours Worked: "))
    hourlyRateA = float(input("Enter Hourly Rate: "))
    print("\n")

    employeeB = input("Enter Employee B Name: ")
    hoursB = float(input("Enter Hours Worked: "))
    hourlyRateB = float(input("Enter Hourly Rate: "))
    print("\n")

    employeeC = input("Enter Employee C Name: ")
    hoursC = float(input("Enter Hours Worked: "))
    hourlyRateC = float(input("Enter Hourly Rate: "))
    print("\n")

    weeklyPayA = hoursA * hourlyRateA
    weeklyPayB = hoursB * hourlyRateB
    weeklyPayC = hoursC * hourlyRateC

    grandPayroll = weeklyPayA + weeklyPayB + weeklyPayC

    print("\n")
    print("Employee A Weekly Pay: $", weeklyPayA)
    print("Employee B Weekly Pay: $", weeklyPayB)
    print("Employee C Weekly Pay: $", weeklyPayC)

    print("Grand Payroll = $", grandPayroll)

    return grandPayroll

grandPayroll()
