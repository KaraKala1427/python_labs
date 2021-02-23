print("Celsius\t | Fahrenheit")

for cell in range(0, 101, 10):
	far = (cell * 9/5) + 32

	print("{}\t | {}".format(cell, far))