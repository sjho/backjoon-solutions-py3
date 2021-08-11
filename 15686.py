from itertools import combinations

N, M = map(int, input().split())

chicken = []
house = []
for i in range(N) :
    for j, n in enumerate(list(map(int, input().split()))) :
        if n == 1 :
            house.append((i, j))
        if n == 2 :
            chicken.append((i, j))

answer = (N+N+1)*len(house)

for cs in combinations(chicken, M) :
    curr = 0
    for h in house :
        min_d = N+N+1
        for c in cs :
            d = abs(c[0]-h[0]) + abs(c[1]-h[1])
            min_d = min(min_d, d)
        curr += min_d
    answer = min(answer, curr)

print(answer)
