n = int(input())

tri = []
dp = []

for i in range(n) :
    tri.append(list(map(int,input().split(' '))))

dp.append(tri[0])

for i in range(1, n) :
    dp.append([])
    for j in range(i+1) :
        if j == 0 :
            dp[i].append(dp[i-1][j]+tri[i][j])
        elif j == i :
            dp[i].append(dp[i-1][j-1]+tri[i][j])
        else :
            dp[i].append(max(dp[i-1][j]+tri[i][j], dp[i-1][j-1]+tri[i][j]))

print(max(dp[n-1]))