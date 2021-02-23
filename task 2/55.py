frequency = float(input("Enter a frequency: "))

name = ""

if frequency < 3e9:
	name = "radio waves"
elif frequency >= 3e9 and frequency < 3e12:
	name = "microwaves"
elif frequency >= 3e12 and frequency < 4.3e14:
	name = "infrared light"
elif frequency >= 4.3e14 and frequency < 7.5e14:
	name = "visible light"
elif frequency >= 7.5e14 and frequency < 3e17:
	name = "ultraviolet light"
elif frequency >= 3e17 and frequency < 3e19:
	name = "x-rays"
elif frequency >= 3e19:
	name = "gamma rays"
	
if name != "":
	print("This frequency is in the '{}'".format(name))
else:
	print("Invalid frequency entered.")