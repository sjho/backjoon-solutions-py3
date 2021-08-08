inp = input()

result = 0
digit = ''
num = 0
minus = False

for c in inp :
    if c.isdigit() :
        digit = digit+c
    else :
        num = int(digit)
        if minus : 
            result = result - num
        else :
            result = result + num
        if c == '-' :
            minus = True

        digit = ''
        
            
num = int(digit)
if minus : 
    result = result - num
else :
    result = result + num
    

print(result)
