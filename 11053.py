n = int(input())
a = list(map(int, input().split(' ')))

dp = []
for i in range(n) :
    dp.append(1)

for i in range(n) :
    max_cnt = dp[i]
    for j in range(i) :
        if a[i] > a[j] :
            max_cnt = max(max_cnt, dp[j]+1)
    dp[i] = max_cnt

print(max(dp))

