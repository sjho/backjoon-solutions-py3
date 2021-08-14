n = int(input())
m = int(input())

INF = 987654321

graph = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(n):
    graph[i][i] = 0

# floyd

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] != INF and graph[k][j] != INF:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    print(" ".join(map(str, map(lambda x: 0 if x == INF else x, graph[i]))))
