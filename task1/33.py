
day_old = int(input("Enter the number of day-old bread loaves = "))
reg = day_old*3.49
dis = day_old*3.49*0.6
price = day_old*3.49 - day_old*3.49*0.6
print("Regular cost of bread = ", "%.2f" % reg)
print("Discount = ", "%.2f" % dis)
print("Price = ", "%.2f" % price)