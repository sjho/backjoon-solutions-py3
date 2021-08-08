inp = input()
n = int(inp)
    

l = []

for i in range(n) :
    l.append(input())

l = list(set(l))
l = sorted(l)
l = sorted(l, key=len)

for i in l :
    print(i)
