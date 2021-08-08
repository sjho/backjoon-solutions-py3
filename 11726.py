inp = input()
n = int(inp)

dp = [1]

for i in range(1, n+1) :
    num = 0
    for j in range(i) :
        if i-j <= 2 and j < len(dp) :
            num = num + dp[j]
    dp.append(num%10007)

print(dp[n])
