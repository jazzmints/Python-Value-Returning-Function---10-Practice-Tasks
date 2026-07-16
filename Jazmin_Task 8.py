#Task 8

def discountedPrice(price, discount):
    return price - discount

finalPrice = discountedPrice(150, 20)

print("Final Price: $", finalPrice)

#Exercise 1

def finalPrice(price, discount):
    return price - discount

price = finalPrice(200, 35)

print("Price = $200")
print("Discount = $35")

print("Final Price: $", price)

#Exercise 2

def askUser():
    productName = input("Enter Product Name: ")
    originalPrice = float(input("Enter Original Price: "))
    discount = float(input("Enter Discount Amount: "))

    finalPrice = originalPrice - discount

    print("Product: ", productName)
    print("Original Price: $", originalPrice)
    print("Discount: $", discount)
    print("Final Price: $", finalPrice)

    return finalPrice

askUser()

#Exercise 3

def fourProducts(product, discount):
    return product - discount 
product1 = fourProducts(90, 10)
product2 = fourProducts(80, 20)
product3 = fourProducts(70, 30)
product4 = fourProducts(60, 40)

totalDiscount = 90+80+70+60
subTotal = 10+20+30+40

finalTotal = product1 + product2 + product3 + product4

print("Subtotal = $", subTotal)
print("Total Discount = $", totalDiscount)
print("Final Total = $", finalTotal)
