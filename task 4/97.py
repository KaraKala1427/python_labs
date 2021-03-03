from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126
res = ""

def randomPassword():
    randomLength = randint(SHORTEST, LONGEST)
    result = ''
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result += randomChar
    
    global res 
    res = result
    return result 

def checkPassword(password):
    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True

    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    
    return False

def main():
    # p = checkPassword(randomPassword())
    # print(p)
    k = 0

    while not checkPassword(randomPassword()):
        k = k + 1
    
    print("Attempts:",k)
    print("Good password:", res)

if __name__ == "__main__":
    main()
