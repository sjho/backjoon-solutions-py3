inp = input()
n = int(inp)

stair = []

for i in range(n) :
    inp = input()
    stair.append(int(inp))

dp = []
for i in range(n+1) :
    dp.append([])
    for j in range(3) :
        dp[len(dp)-1].append(0)

if n == 1 :
    print(stair[0])
else :
    dp[1][1] = stair[0]
    dp[2][1] = stair[1]

    for i in range(2, n+1) :
        dp[i][1] = max(dp[i-2][1], dp[i-2][2])+stair[i-1]
        dp[i][2] = dp[i-1][1]+stair[i-1]
    
    print(max(dp[n][1], dp[n][2]))
