year =  int(input("Enter a year: "))

leap = False

if year % 400 == 0:
	leap = True
elif year % 100 == 0 and not year % 400 == 0:
	leap = False 
elif year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
	leap = True 

if leap:
	print("Yes, it is leap year.")
else:
	print("No, it is not leap year.")