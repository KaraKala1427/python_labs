import random 
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] 
number = random.randrange(37) 
print("The spin resulted in", number) 
if number == '00' or number =='0': 
    print('Pay 0') 
else: 
    number = int(number) 
    color="" 
    if number in red: 
       color = "Red" 
    else: 
        color = "Black" 
    print("Pay ",number) 
    print("Pay",color) 
    print("Pay Odd") if number%2 else print("Pay Even") 
    print("1 to 18") if number<19 else print("19 to 36")