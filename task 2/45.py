col = input("Enter the column: ")
row = int(input("Enter the row: "))

if col in "aceg":
    col_start_black = True
else: 
    col_start_black = False

if col_start_black:

    if row % 2 == 0:
        white = True
    else:
        white = False

else:
    
	if row % 2 == 0:
		white = False
	else:
		white = True

if white:
    print("Cell is white.")
else:
	print("Cell is black.")
