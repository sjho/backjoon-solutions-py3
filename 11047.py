inp = input()
inp = inp.split()

n = int(inp[0])
k = int(inp[1])

ai = []
ai_check = []

for i in range(n) :
    ai.append(int(input()))
    ai_check.append(0)

t = 0

while k > 0 :
    for i in range(t, n) :
        a = ai[n-1-i]
        if a <= k :
            ai_check[n-1-i] = k//a
            k = k%a
            break
        else :
            t = t+1

print(sum(ai_check))
