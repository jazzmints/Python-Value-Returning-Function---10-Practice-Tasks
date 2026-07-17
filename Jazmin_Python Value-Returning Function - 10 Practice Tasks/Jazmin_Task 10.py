#Task 10

def calculateAssets(liabilities, equity):
    return liabilities + equity

assets = calculateAssets(25000, 75000)

print("Assets: ", assets)
print("\n")

#Exercise 1

def returnAssets(liabilities, equity):
    return liabilities + equity

assets = returnAssets(40000, 60000)

print("Assets: ", assets)
print("\n")

#Exercise 2

def askUser():
    companyName = input("Enter Company Name: ")
    liabilities = float(input("Enter Liabilities Amount:"))
    equity = float(input("Enter Equity Amount: "))

    print("\n")

    assets = liabilities + equity

    print("--- ", companyName, " ---")
    print("Assets: ", assets)
    print("Liabilities: ", liabilities)
    print("Equity: ", equity)

    return assets
askUser()
print("\n")

#Exercise 3

def threeCompanies():
    companyA =  input("Enter Company Name: ")
    liabilitiesA = float(input("Enter Liabilities Amount:"))
    equityA = float(input("Enter Equity Amount: "))
    
    print("\n")

    assetsA = liabilitiesA + equityA

    companyB =  input("Enter Company Name: ")
    liabilitiesB = float(input("Enter Liabilities Amount:"))
    equityB = float(input("Enter Equity Amount: "))
    
    print("\n")

    assetsB = liabilitiesB + equityB

    companyC =  input("Enter Company Name: ")
    liabilitiesC = float(input("Enter Liabilities Amount:"))
    equityC = float(input("Enter Equity Amount: "))
    
    print("\n")

    assetsC = liabilitiesC + equityC


    print("--- ", companyA, " ---")
    print("Assets: ", assetsA)
    print("\n")

    print("--- ", companyB, " ---")
    print("Assets: ", assetsB)
    print("\n")
    
    print("--- ", companyC, " ---")
    print("Assets: ", assetsC)

    return assetsA and assetsB and assetsC
threeCompanies()