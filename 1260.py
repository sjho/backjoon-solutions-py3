inp = input()
inp = inp.split(' ')

n = int(inp[0])
m = int(inp[1])
v = int(inp[2])

graph = []
for i in range(n):
    graph.append([])

for i in range(m):
    inp = input()
    inp = inp.split(' ')
    
    n1 = int(inp[0])
    n2 = int(inp[1])
    graph[n1-1].append(n2)
    graph[n2-1].append(n1)

for i in range(n):
    graph[i] = list(set(graph[i]))
    graph[i] = sorted(graph[i])

dfs = [v]
dfs_result = []

while dfs != [] :
    current = dfs[len(dfs)-1]
    if current not in dfs_result :
        dfs_result.append(current)
    added = False
    for node in graph[current-1] :
        if node not in dfs_result and node not in dfs :
            dfs.append(node)
            added = True
            break
    if not added :
        del dfs[len(dfs)-1]

bfs = [v]
bfs_result = []

while bfs != [] :
    current = bfs[0]
    bfs_result.append(current)
    del bfs[0]
    for node in graph[current-1] :
        if node not in bfs_result and node not in bfs :
            bfs.append(node)

for node in dfs_result :
    print(node, end=' ')
print()
for node in bfs_result :
    print(node, end=' ')
print()