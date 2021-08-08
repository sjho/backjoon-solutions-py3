import math

inp = input()
inp = inp.split(' ')

a = int(inp[0])
b = int(inp[1])
v = int(inp[2])

h = v-a
n = math.ceil(h/(a-b))

print(n+1)

