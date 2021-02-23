mag = float(input('Please enter the scale of magnitude:'))

dec = ""

if mag < 2:
    dec = "Micro"
elif mag >= 2 and mag < 3:
    dec = "Vey minor"
elif mag >= 3 and mag < 4:
    dec = "Minor"
elif mag >= 4 and mag < 5:
    dec = "Light"
elif mag >= 5 and mag < 6:
    dec = "Moderate"
elif mag >= 6 and mag < 7:
    dec = "Strong"
elif mag >= 7 and mag < 8:
    dec = "Major"
elif mag >= 8 and mag < 10:
    dec = "Great"
elif mag >=10:
    dec = "Meteoric"


print("This earthquake is classified as '{}'. ".format(dec))