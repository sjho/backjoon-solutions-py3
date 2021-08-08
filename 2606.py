n = int(input())
t = int(input())

graph = []
graph_s = []

for i in range(n+1) :
    graph.append([])
    graph_s.append(False)
    for j in range(n+1) :
        graph[len(graph)-1].append(False)

for i in range(t) :
    inp = input().split(' ')
    c1 = int(inp[0])
    c2 = int(inp[1])

    graph[c1][c2] = True
    graph[c2][c1] = True

bfs = [1]
c = 0


while c < len(bfs) :
    graph_s[bfs[c]] = True
    for i, k in enumerate(graph[bfs[c]]) :
        if not graph_s[i] and k :
            bfs.append(i)
    c = c+1

print(len(list(set(bfs)))-1)
    
    
