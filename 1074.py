inp = input()
inp = inp.split()

n = int(inp[0])
r = int(inp[1])
c = int(inp[2])

edge = int(pow(2, n))

ans = 0

while r>0 or c>0 :
    edge = edge//2
    if r//edge == 0 and c//edge > 0 :
        ans = ans + edge*edge
    elif r//edge > 0 and c//edge == 0 :
        ans = ans + edge*edge*2
    elif r//edge > 0 and c//edge > 0:
        ans = ans + edge*edge*3
    r = r%edge
    c = c%edge

print(ans)
