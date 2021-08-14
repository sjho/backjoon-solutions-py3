import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a-1].append([c, b-1])

start, end = map(int, input().split())
start = start - 1
end = end - 1

# bfs

node = []
d = [float('inf') for _ in range(n)]
d[start] = 0

heapq.heappush(node, [d[start], start])

while node:
    curr_d, curr_n = heapq.heappop(node)
    if d[curr_n] < curr_d:
        continue

    for n in graph[curr_n]:
        distance = d[curr_n] + n[0]
        if distance < d[n[1]]:
            d[n[1]] = distance
            heapq.heappush(node, [distance, n[1]])

print(d[end])

