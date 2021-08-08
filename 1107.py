inp = input()
n = int(inp)
inp = input()
m = int(inp)
broken = []
if m != 0 :
    inp = input()
    broken = inp.split()
    broken = list(map(int, broken))
    broken = sorted(broken)

ans = abs(n-100)

for i in range(1000001):
    ok = True
    temp = i
    if i == 0 and 0 in broken:
        continue
    while temp > 0 :
        if temp % 10 in broken :
            ok = False
            break
        temp = temp // 10
    if ok :
        ans = min(ans, abs(n-i)+int(len(str(i))))

print(ans)
