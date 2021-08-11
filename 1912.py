inp = input()
n = int(inp)

inp = input()
inp = inp.split()
inp = list(map(int, inp))

dp = inp.copy()

max_num = max(inp)


for i in range(1, n):
    if dp[i-1] > 0 and dp[i] + dp[i-1] > 0 :
        dp[i] = dp[i] + dp[i-1]
    max_num = max(dp[i], max_num)
    

print(max_num)