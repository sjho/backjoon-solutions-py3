inp = input()
n = int(inp)

inp = input()
inp = inp.split()
pi = map(int, inp)
pi = sorted(pi)

result = 0
for i in range(n) :
    result = result + sum(pi[:i+1])

print(result)
    
