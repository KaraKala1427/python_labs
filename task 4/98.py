def hex2int(hexa): 
    H = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    h = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    decimal = 0
    
    while True: 
        for i in hexa:
            if  (i in h) or (i in H):
                continue
            else: 
                print("Wrong format of hexadecimal")
                hexa = input("Enter hexadecimal: ")
                break
        else: 
            break
    
    for i in range(len(hexa)):
        
        exp = len(hexa) - i -1
        if hexa[i] in h: 
            value = h.index(hexa[i])
        elif hexa[i] in H: 
            value = h.index(hexa[i])
        decimal = decimal + value*16**exp
        
    return decimal 

def int2hex(inter):
    while True: 
        try:
            inter = int(inter)
        except ValueError:
            inter = input("Enter deciaml from 0 to 15: ")
            continue
        else:
            inter = int(inter)
            break
    h = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return h[inter]

print(hex2int(input("Enter hex: ")))
print(int2hex(input("Enter decimal: ")))