inp = input().split(' ')
n = int(inp[0])
m = int(inp[1])

graph = []

for i in range(n) :
    inp = input().split(' ')
    graph.append(list(map(int, inp)))

zeros = []
twos = []

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            zeros.append([i, j])
        if graph[i][j] == 2 :
            twos.append([i, j])

zeros_len = len(zeros)
result = 0

def virus(graph, z1, z2, z3, r) :
    bfs = twos.copy()
    safe = 0
    checked = []

    for i in range(n) :
        checked.append([])
        for j in range(m) :
            if (z1[0] == i and z1[1] == j)\
                or (z2[0] == i and z2[1] == j)\
                or (z3[0] == i and z3[1] == j) :
                checked[-1].append(True)
            else :
                checked[-1].append(False)

    t = 0
    while t < len(bfs) :
        i = bfs[t][0]
        j = bfs[t][1]
        t = t+1
        if checked[i][j] :
            continue
        checked[i][j] = True
        
        if i-1 >= 0 and graph[i-1][j] == 0 and not checked[i-1][j] :
            bfs.append([i-1, j])
        if j-1 >= 0 and graph[i][j-1] == 0 and not checked[i][j-1] :
            bfs.append([i, j-1])
        if i+1 < n and graph[i+1][j] == 0 and not checked[i+1][j] :
            bfs.append([i+1, j])
        if j+1 < m and graph[i][j+1] == 0 and not checked[i][j+1] :
            bfs.append([i, j+1])

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 and not checked[i][j] :
                safe = safe + 1
    
    return safe


for i in range(zeros_len) :
    for j in range(i+1, zeros_len) :
        for k in range(j+1, zeros_len) :
            result = max(result, virus(graph, zeros[i], zeros[j], zeros[k], result))

print(result)

