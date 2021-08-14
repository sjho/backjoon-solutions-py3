import sys
sys.setrecursionlimit(10**9)

N = int(input())

graph = [set() for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())

    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)

parents = [-1 for _ in range(N)]
cache = [False for _ in range(N)]

def dfs(i):
    cache[i] = True
    nodes = list(graph[i])

    for n in nodes:
        if not cache[n]:
            parents[n] = i
            dfs(n)

dfs(0)

for p in parents[1:]:
    print(p+1)

