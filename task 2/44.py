month = int(input("Please enter in a month with a numerical value (1-12): "))
date = int(input("Please enter in a date: "))

holiday = ""

if month == 1 or month == 7 or month == 12:
	if month == 1 and date == 1:
		holiday = "New Year's Day"
	elif month == 7 and date == 1:
		holiday = "Canada Day"
	elif month == 12 and date == 25:
		holiday = "Christmas Day"
		
if holiday == "":
	print("There is no holiday in that day and month")
else:
	print("That holdiday's name is {}.".format(holiday)) 