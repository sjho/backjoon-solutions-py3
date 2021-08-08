t_inp = input()

dp = [1]

for i in range(1, 11) :
    num = 0
    for j in range(i) :
        if i-j <= 3 and j < len(dp) :
            num = num + dp[j]
    dp.append(num)


for t in range(int(t_inp)):
    inp = input()
    n = int(inp)

    print(dp[n])
