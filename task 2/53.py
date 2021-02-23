rate = float(input("Enter the rating : "))
if rate == 0:
    print("Unacceptable performance")
elif rate>0 and rate<0.4 or rate>0.4 and rate<0.6:
    print("Error")
elif rate == 0.4:
    print("Acceptable performance", "Employee's raise= $", 2400*0.4)
elif rate >= 0.6:
    print("Meritorious performance", "Employee's raise= $", 2400*0.6)