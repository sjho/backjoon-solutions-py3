inp = input()
o = int(inp)
a = 0

while a < o :
    b = a
    c = a
    while c > 0:
        b = b+c%10
        c = c//10
    if o == b:
        print(a)
        break
    else :
        a = a+1

if a >= o :
    print(0)
