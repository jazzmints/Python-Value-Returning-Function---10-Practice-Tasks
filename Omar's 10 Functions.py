#1-1
def add_numbers(x, y):
    return x+y
    
answer = add_numbers(18, 42)

print("Answer:", answer)

#1-2
def add_nums():
    x = int(input("first number:"))
    y = int(input("second number:"))
    return x + y
    
answer = add_nums()

print("the total is:", answer)

#1-3
def add_nums():
    x = int(input("Enter number:"))
    y = int(input("Enter number:"))
    z = int(input("Enter number:"))
    return x+y+z
    
total = add_nums()

print("Total", total)

#2-1
def mult_num(a,b):
    return a*b
    
answer = mult_num(12,7)

print(answer)

#2-2
def cal_area():
    w = int(input("Width:"))
    h = int(input("Height:"))
    return w*h

answer = cal_area()

print("area:", answer)

#2-3
def vol(l,w,h):
    return l*w*h
    
answer = vol(5,8,6)
print("Volume:", answer)

#3-1
def area_of(l,w):
    return l*w

area_of(9,6)

#3-2

def area():
    a = int(input("length:"))
    b = int(input("width"))
    return a*b

area()

#3-3
def rec1():
    a = int(input("1st rectangle length:"))
    b = int(input("1st rectangle width:"))
    return a*b

def rec2() :   
    c = int(input("2nd rectangle length:"))
    d = int(input("2nd rectangle width:"))
    return c*d

def rec3():    
    e = int(input("3rd rectangle length:"))
    f = int(input("3rd rectangle length:"))
    return e*f
    
area1 = rec1()
area2 = rec2()
area3 = rec3()

print("Rectangle 1 Area =",area1)
print("Rectangle 2 Area =",area2)
print("Rectangle 3 Area =",area3)
print("Total Area =",area1 + area2 + area3)

#4-1
def pay(h,w):
    return h*w

pay(40,22)

#4-2
def name_pay():
    w = int(input("How many hours work:"))
    r = int(input("Pay rate:"))
    return w*r

empl = input("Name:")
weekly = name_pay()

print("Employee:",empl)
print("Weekly Pay = $", weekly)

#4-3
def pay1():
    w = int(input("How many hours work:"))
    r = int(input("Pay rate:"))
    return w*r

def pay2():
    w = int(input("How many hours work:"))
    r = int(input("Pay rate:"))
    return w*r

def pay3():
    w = int(input("How many hours work:"))
    r = int(input("Pay rate:"))
    return w*r

empl_a = pay1()
empl_b = pay2()
empl_c = pay3()

print("Employee A",empl_a)
print("employee B",empl_b)
print("Employee C",empl_c)
print("Grand Payroll =$",empl_a+empl_b+empl_c)

#5-1
def stud_av(sco1,sco2,sco3):
    return (sco1+sco2+sco3) / 3

stud_av(90,85,100)

#5-2
def stud():
    a = int(input("English Score:"))
    b = int(input("History Score:"))
    c = int(input("Science Score:"))
    d = int(input("Math Score:"))
    e = int(input("Spanish Score:"))
    return (a+b+c+d+e)/5

stud()

#5-3
def gra_av():
    a = int(input("Score:"))
    b = int(input("Score:"))
    c = int(input("Score:"))
    return (a+b+c)/3

average = gra_av()
print("Average =", average)

if average > 90:
    print("Grade = A")
elif average > 80:
    print("Grade = B")
elif average > 70:
    print("Grade = C")
elif average > 60:
    print("Grade = D")
else:
    print("Grade = F")

#6-1
def hours_to_min(x):
    return x * 60

minutes = hours_to_min(5)
print("Minutes:",minutes)

#6-2
def hours_min():
    h = int(input("How many hours worked:"))
    print("Hours:",h)
    return h*60

hours = hours_min()
print("Minutes",hours)

#6-3
def hours():
    h = int(input("How many hours worked:"))
    return h

hour = hours()
print("Hours =",hour)
print("Minutes =",hour*60)
print("Seconds =",hours*3600)

#7-1
def cel_fer(cel):
    return (cel * 9 / 5) + 32

fer = cel_fer(20)
print("Temperature:", fer)

#7-2
def temp():
    cel = int(input("Temp Celsius:"))
    return (cel *9 / 5)+32

fah = temp()

print("Temp Fahrenheit:", fah)
print("Temp Celsius:",(fah - 32) * 5 / 9)

#7-3
def temperature():
    cel = int(input("Temp Celsius:"))
    return (cel *9 / 5)+32

fahr = temperature()
print("Temp Fahrenheit:", fahr)
print("Temp Celsius:",(fahr - 32) * 5 / 9)
if fahr > 80:
    print("Hot")
elif fahr > 55:
    print("Warm")
elif fahr > 32:
    print("Cold")
else:
    print("Freeze")

#8-1
def disc_price(p,d):
    return p-d

final_price = disc_price(200,50)
print("Final Price: $",final_price)

#8-2
prod_name = input("Product name:")
og_price = int(input("Product price:"))
disc = int(input("Discount amount:"))

def disc_name():
    return og_price - disc

fin_pri = disc_name()

print(prod_name)
print("Original Price:",og_price)
print("Discount:",disc)
print("Final Price: $",fin_pri)

#8-3
pri1 = int(input("1st Product:"))
dis1 = int(input("1st Discount:"))
pri2 = int(input("2nd Product:"))
dis2 = int(input("2nd Discount:"))
pri3 = int(input("3rd Product:"))
dis3 = int(input("3rd Discount:"))
pri4 = int(input("4th Product:"))
dis4 = int(input("4th Discount:"))

def pric():
    return pri1+pri2+pri3+pri4

def disco():
    return dis1+dis2+dis3+dis4

subto = pric()
discount = disco()

print("Subtotal: $",subto)
print("Total Discount: $",discount)
print("Final Total: $", subto - discount)

#9-1
def int(p,r,t):
    return (p*r*t)/100

interest = int(5000,5, 3)

print("Interest:",interest)

#9-2
principal = int(input("Principle:"))
rate = int(input("Rate:"))
time = int(input("Time:"))

def inter():
    return (principal + rate + time) / 100

sim_int = inter()
print("Interest:", sim_int)

#9-3
interest1 = int(input("Interest amount:"))

def prin_int():
    princip = int(input("Principle:"))
    return princip + interest1

final_amount = prin_int()

print("Interest:",interest1)
print("Final Amount:", final_amount)

#10-1
def assets(l,e):
    return l+e

real_assets = assets(25000,75000)

print("Assets:",real_assets)

#10-2
comp_nam = input("Company name:")
liab = int(input("Liabilities:"))
equity = int(input("Equity:"))

def cal_asset():
    return liab + equity

true_asset = cal_asset()

print("Company name:",comp_nam)
print("Asset:", true_asset)
print("Liabilities:", liab)
print("Equity:",equity)

#10-3
comp1 = input("Company A:")
com1_as = int(input("Company A Asset:"))
comp2 = input("Company B:")
com2_as = int(input("Company B Asset:"))
comp3 = input("Company C:")
com3_as = int(input("Company C Asset:"))

def comb_as():
    return com1_as+com2_as+com3_as

combine_assets = comb_as()

print("Company A:", comp1)
print("Company A Assets: $",com1_as)
print("Company B:", comp2)
print("Company B Assets: $",com2_as)
print("Company C:", comp3)
print("Company C Assets: $",com3_as)
print("Combined Assets: $",combine_assets)