inp = input()
inp = inp.split()

a = int(inp[0])
b = int(inp[1])
c = max(a, b)
d = min(a, b)

while d != 0:
    mod = c % d
    c = d
    d = mod
    
print(c)

print(a*b//c)
