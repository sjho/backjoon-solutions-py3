n = int(input())
house = []
dp = []

for i in range(n) :
    house.append(list(map(int, input().split(' '))))
    dp.append([])

dp[0] = house[0].copy()

for i in range(1, n) :
    dp[i].append(min(dp[i-1][1]+house[i][0], dp[i-1][2]+house[i][0]))
    dp[i].append(min(dp[i-1][0]+house[i][1], dp[i-1][2]+house[i][1]))
    dp[i].append(min(dp[i-1][0]+house[i][2], dp[i-1][1]+house[i][2]))

print(min(dp[n-1]))