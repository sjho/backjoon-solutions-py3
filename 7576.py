inp = input().split(' ')
m = int(inp[0])
n = int(inp[1])

graph = []

bfs_i = []
bfs_j = []

for i in range(n) :
    inp = input()
    g = list(map(int, inp.split(' ')))
    graph.append(g)
    for j, t in enumerate(g) :
        if t == 1:
            bfs_i.append(i)
            bfs_j.append(j)


t = 0

while t < len(bfs_i) :
    i = bfs_i[t]
    j = bfs_j[t]
    
    t = t+1
    
    if i-1 >= 0 and graph[i-1][j] == 0 :
        bfs_i.append(i-1)
        bfs_j.append(j)
        graph[i-1][j] = graph[i][j]+1
    if j-1 >= 0 and graph[i][j-1] == 0 :
        bfs_i.append(i)
        bfs_j.append(j-1)
        graph[i][j-1] = graph[i][j]+1
    if i+1 < n and graph[i+1][j] == 0 :
        bfs_i.append(i+1)
        bfs_j.append(j)
        graph[i+1][j] = graph[i][j]+1
    if j+1 < m and graph[i][j+1] == 0 :
        bfs_i.append(i)
        bfs_j.append(j+1)
        graph[i][j+1] = graph[i][j]+1


ripen = True
result = 0

for i in range(n):
    if not ripen :
        break
    for j in range(m):
        if graph[i][j] == 0 :
            result = 0
            ripen = False
            break
        if result < graph[i][j] :
            result = graph[i][j]

print(result-1)
