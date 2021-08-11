N = int(input())
A = list(map(int, input().split()))

dp_1 = [1] * N
dp_2 = [1] * N

# dp 1
for i in range(N) :
    for j in range(i):
        if A[j] < A[i] :
            dp_1[i] = max(dp_1[i], dp_1[j]+1)

# dp 2
for i in range(N-1, -1, -1) :
    for j in range(N-1, i-1, -1):
        if A[j] < A[i] :
            dp_2[i] = max(dp_2[i], dp_2[j]+1)

answer = 0

for i in range(N) :
    answer = max(answer, dp_1[i]+dp_2[i]-1)

print(answer)