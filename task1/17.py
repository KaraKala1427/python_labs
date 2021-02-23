print("Enter the liters of water")
w = input()
print("Enter the temperature")
t = input()
c = 4186
Q = c * int(t) * int(w)
P = Q/3600000 * 8.9
print("You need ",Q, "joules")
print("The price for the electricity is ", "%.2f"%P, "cents")





