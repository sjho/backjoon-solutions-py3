inp = input()
inp = inp.split()

n = int(inp[0])
m = int(inp[1])

graph = []
check = []
bfs_i = [0]
bfs_j = [0]
bfs_l = [1]

for i in range(n) :
    inp = input()
    graph.append([])
    check.append([])
    for j in inp :
        graph[len(graph)-1].append(int(j))
        check[len(check)-1].append(False)

t = 0

while t < len(bfs_i):
    i = bfs_i[t]
    j = bfs_j[t]
    l = bfs_l[t]
    
    if check[i][j] :
        t = t+1
        continue
    check[i][j] = True
    

    if j-1 >= 0 and graph[i][j-1] == 1 and not check[i][j-1] :
        if i == n-1 and j-1 == m-1 :
            print(l+1)
            break
        bfs_i.append(i)
        bfs_j.append(j-1)
        bfs_l.append(l+1)
    if i-1 >= 0 and graph[i-1][j] == 1 and not check[i-1][j] :
        if i-1 == n-1 and j == m-1 :
            print(l+1)
            break
        bfs_i.append(i-1)
        bfs_j.append(j)
        bfs_l.append(l+1)
    if j+1 < m and graph[i][j+1] == 1 and not check[i][j+1] :
        if i == n-1 and j+1 == m-1 :
            print(l+1)
            break
        bfs_i.append(i)
        bfs_j.append(j+1)
        bfs_l.append(l+1)
    if i+1 < n and graph[i+1][j] == 1 and not check[i+1][j] :
        if i+1 == n-1 and j == m-1 :
            print(l+1)
            break
        bfs_i.append(i+1)
        bfs_j.append(j)
        bfs_l.append(l+1)

    t = t+1
    
    
