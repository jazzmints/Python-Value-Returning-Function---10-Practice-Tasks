#Task 7

def celsiusToFarenheit (celsius):
    return (celsius * 9 / 5) + 32

temperature = celsiusToFarenheit(25)

print("Temperature: ", temperature)

#Exercise 1 

def farenheitToCelsius (farenheit):
    return(farenheit - 32) * 5 / 9

temp = farenheitToCelsius(30)

print(temp, "°")

#Exercise 2

def celsTemp ():
    celsius = float(input("Enter Temperature in C°: "))
    print("\n")

    farenheit = (celsius * 9 / 5) + 32
    
    print("Temperature (C°): ", celsius, "°")
    print("Temperature (F°): ", farenheit, "°")

    return farenheit
celsTemp()
print("\n")

#Exercise 3


def tempCheck ():
    print("--- Temperature Options ---")
    print("1. Celsius")
    print("2. Farenheight")

    choiceOfTemp = int(input("Enter Choice Of Temperature: "))
    print("\n")

    if choiceOfTemp == 1:
        celsius = float(input("Enter Temperature in Celsius: "))
        
        print("Celsius: ", celsius, "°")
        print("Farenheight: ", ((celsius * 9 / 5) + 32), "°")

        if celsius > 70:
            print("Weather: Hot ")
        elif celsius > 37:
            print("Weather: Warm")
        else:
            print("Weather: Cold")
    
    elif choiceOfTemp == 2:
        farenheit = float(input("Enter Temperature in Celsius: "))
        
        print("Farenheight: ", farenheit, "°")
        print("Celsius: ",((farenheit-34)* 9 / 5), "°")

        if farenheit > 80:
            print("Weather: Hot ")
        elif farenheit > 60:
            print("Weather: Warm")
        else:
            print("Weather: Cold")

tempCheck()