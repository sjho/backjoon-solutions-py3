t = int(input())

while t != 0 :
    n = int(input())
    sticker = []
    dp = []
    for _ in range(2) :
        sticker.append(list(map(int, input().split(' '))))
    
    dp.append([sticker[0][0], sticker[1][0]])
    for i in range(1, n) :
        dp.append([])
        dp[i].append(max(dp[i-1][0], dp[i-1][1]+sticker[0][i]))
        dp[i].append(max(dp[i-1][1], dp[i-1][0]+sticker[1][i]))
    
    print(max(dp[-1]))

    t = t - 1