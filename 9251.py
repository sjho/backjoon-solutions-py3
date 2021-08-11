a = input()
b = input()

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i, c1 in enumerate(a) :
    for j, c2 in enumerate(b) :
        if c1 == c2 :
            dp[i+1][j+1] = dp[i][j] + 1
        else :
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[-1][-1])