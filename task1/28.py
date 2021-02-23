print("Inter the numbers")
import math
T = int(input())
v = float(input())
if T >= 10:
    print("wrong temperature")
elif v < 4.8:
    print("wrong speed")
else:
    WCI = 13.12 + 0.6215 * T - 11.37 * (v ** 0.16) + 0.3965 * T * (v ** 0.16)
    print(WCI)


