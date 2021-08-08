inp = input()
inp = inp.split(' ')

n = int(inp[0])
k = int(inp[1])

if k == 0:
    print(1)
else :
    temp = 0
    for i in range(n, n-k, -1):
        if temp == 0:
            temp = i
        else :
            temp = temp*i

    for i in range(k, 0, -1):
        temp = temp//i

    print(temp)
