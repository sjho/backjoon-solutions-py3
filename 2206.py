N, M = map(int, input().split())

map_input = []
map_search = []

for _ in range(N):
    map_input.append(list(map(int, list(input()))))
    map_search.append([[-1, -1] for _ in range(M)])

# bfs
queue = [(0, 0, 0)]
i = 0
ok = False

map_search[0][0] = [1, 1]
ds = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while i < len(queue):
    x, y, w = queue[i]
    i = i+1

    for d in ds:
        dx = x+d[0]
        dy = y+d[1]
        if 0 <= dx < N and 0 <= dy < M:
            if map_input[dx][dy] == 0 and map_search[dx][dy][w] == -1:
                map_search[dx][dy][w] = map_search[x][y][w] + 1
                queue.append((dx, dy, w))
            elif map_input[dx][dy] == 1 and w == 0 and map_search[dx][dy][1] == -1:
                map_search[dx][dy][1] = map_search[x][y][w] + 1
                queue.append((dx, dy, 1))

a1, a2 = map_search[N-1][M-1]

if a1 == -1 and a2 != -1:
    print(a2)
elif a2 == -1 and a1 != -1:
    print(a1)
else:
    print(min(a1, a2))
