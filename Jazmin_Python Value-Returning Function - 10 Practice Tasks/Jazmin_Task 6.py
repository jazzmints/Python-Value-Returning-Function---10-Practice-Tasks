#Task 6

def hoursToMinutes(hours):
    return hours * 60

minutes = hoursToMinutes(3)

print("Minutes: ", minutes)
print("\n")

#Exercise 1 \
def minutesToHours(minutes):
    return minutes // 60

hours = minutesToHours(180)

print("Hours: ", hours)
print("\n")

#Exercise 2

def enterHours():
    hours = int(input("Enter Hours: "))
    return hours * 60

print("Minutes:", enterHours())
print("\n")

#Exercise 3

def hoursToMinutesAndSeconds(hours):
    minutes = hours * 60
    seconds = minutes * 60

    print("Hours = ", hours)
    print("Minutes = ", minutes)
    print("Seconds = ", seconds)

    return minutes and seconds

hoursToMinutesAndSeconds(2)