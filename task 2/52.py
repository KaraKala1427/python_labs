gpa = float(input("Enter a number of grade gpa: "))

grade = ""

if gpa >= 0 and gpa < 0.5:
	grade = "F"
elif gpa >= 0.5 and gpa < 1.15:
	grade = "D"
elif gpa >= 1.5 and gpa < 1.5:
	grade = "D+"
elif gpa >= 1.5 and gpa < 1.85:
	grade = "C-"
elif gpa >= 1.85 and gpa < 2.15:
	grade = "C"
elif gpa >= 2.15 and gpa < 2.5:
	grade = "C+"
elif gpa >= 2.5 and gpa < 2.85:
	grade = "B-"
elif gpa >= 2.85 and gpa < 3.15:
	grade = "B"
elif gpa >= 3.15 and gpa < 3.5:
	grade = "B+"
elif gpa >= 3.5 and gpa < 3.85:
	grade = "A-"
elif gpa >= 3.85 and gpa < 4.0:
	grade = "A"
elif gpa >= 4.0:
	grade = "A+"
	
if grade != "":
	print("The grade is an {}".format(grade))
else:
	print("Invalid number of grade gpa entered.")