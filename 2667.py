inp = input()
n = int(inp)

graph = []
house = []
for i in range(n) :
    inp = input()
    graph.append([])
    house.append([])
    for j in inp :
        graph[len(graph)-1].append(int(j))
        house[len(house)-1].append(0)

current = 1
houses = []
for i in range(n) :
    for j in range(n) :
        if house[i][j] == 0 and graph[i][j] == 1 :
            t = 0
            house_num = 0
            bfs_i = [i]
            bfs_j = [j]
            while t < len(bfs_i) :
                c_i = bfs_i[t]
                c_j = bfs_j[t]

                if house[c_i][c_j] != 0 :
                    t = t+1
                    continue
                house[c_i][c_j] = current
                house_num = house_num + 1

                if c_i-1 >= 0 and house[c_i-1][c_j] == 0 and graph[c_i-1][c_j] == 1 :
                    bfs_i.append(c_i-1)
                    bfs_j.append(c_j)
                if c_j-1 >= 0 and house[c_i][c_j-1] == 0 and graph[c_i][c_j-1] == 1 :
                    bfs_i.append(c_i)
                    bfs_j.append(c_j-1)
                if c_i+1 < n and house[c_i+1][c_j] == 0 and graph[c_i+1][c_j] == 1 :
                    bfs_i.append(c_i+1)
                    bfs_j.append(c_j)
                if c_j+1 < n and house[c_i][c_j+1] == 0 and graph[c_i][c_j+1] == 1 :
                    bfs_i.append(c_i)
                    bfs_j.append(c_j+1)

                t = t+1

            houses.append(house_num)
            current = current + 1

houses = sorted(houses)

print(len(houses))
for h in houses :
    print(h)

