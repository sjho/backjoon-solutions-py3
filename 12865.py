N, K = map(int, input().split())

DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1) :
    W, V = map(int, input().split())
    for j in range(K+1) :
        v = DP[i-1][j]
        if j - W >= 0 :
            v = max(v, DP[i-1][j - W] + V)
        DP[i][j] = v

print(DP[N][K])