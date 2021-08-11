inp = input()
inp = inp.split(' ')

n = int(inp[0])
m = int(inp[1])

graph = []
for i in range(n) :
    graph.append([])

for i in range(m) :
    inp = input()
    inp = inp.split(' ')

    n1 = int(inp[0])
    n2 = int(inp[1])

    if n2 not in graph[n1-1] :
        graph[n1-1].append(n2)

    if n1 not in graph[n2-1] :
        graph[n2-1].append(n1)
    
min_result = -1
min_kevin = -1

for p in range(1, n+1) :
    result = 0
    for g in range(1, n+1) :
        if p == g :
            continue

        stop = True
        bfs = [p]
        bfs_n = [0]
        searched = []

        temp = 0

        while bfs != [] and stop :
            current = bfs[0]
            current_n = bfs_n[0]
            searched.append(current)
            del bfs[0]
            del bfs_n[0]
            for node in graph[current-1]:
                if node == g :
                    temp = current_n+1
                    result += current_n+1
                    stop = False
                elif node not in bfs and node not in searched :
                    bfs.append(node)
                    bfs_n.append(current_n+1)

    if min_result == -1 or min_result > result :
        min_result = result
        min_kevin = p

print(min_kevin)



    