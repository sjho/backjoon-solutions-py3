import sys
from heapq import heappop, heappush
r = sys.stdin.readline
INF = sys.maxsize

def dijkstra(v, k, g) :
    dist = [INF]*v
    queue = []
    dist[k-1] = 0
    heappush(queue, [0, k-1])

    while queue :
        wei, i = heappop(queue)

        if wei > dist[i] :
            continue

        for w, j in g[i] :
            w = w + wei
            if w < dist[j] :
                dist[j] = w
                heappush(queue,[w, j])

    return dist

V, E = map(int, r().split())
K = int(r())
graph = [[] for _ in range(V)]
for _ in range(E) :
    u, v, w = map(int, r().split())
    graph[u-1].append([w, v-1])

for p in dijkstra(V, K, graph) :
    print(p if p != INF else "INF")
