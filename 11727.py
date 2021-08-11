n = int(input())

dp = [1]

for i in range(1, n+1) :
    num = 0
    if i-1 >= 0 :
        num = num + dp[i-1]
    if i-2 >= 0 :
        num = num + dp[i-2] * 2
    dp.append(num%10007)

print(dp[n])