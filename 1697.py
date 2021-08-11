inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])

check = []
bfs = [n]
sec = [0]
t = 0

for i in range(0, 100001) :
    check.append(False)

while t < len(bfs) :
    b = bfs[t]
    s = sec[t]
    t = t+1

    if b == m :
        print(s)
        break
    if check[b] :
        continue
    check[b] = True

    walk1 = b-1
    walk2 = b+1
    warp = b*2

    if 0 <= walk1 <= 100000 and not check[walk1] :
        bfs.append(walk1)
        sec.append(s+1)
    if 0 <= walk2 <= 100000 and not check[walk2] :
        bfs.append(walk2)
        sec.append(s+1)
    if 0 <= warp <= 100000 and not check[warp] :
        bfs.append(warp)
        sec.append(s+1)