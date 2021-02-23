print("Total Price?")
a = input()
Tip = float(int(a) * 0.18)
d = int(a) - Tip
Tax = float(d * 0.1)
print("Tip = ", "%.2f"%Tip)
print("Tax = ", "%.2f"%Tax)
print("Your Total Price = ", "%.2f"%int(a))
