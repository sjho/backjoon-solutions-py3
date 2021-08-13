a, b, c = map(int, input().split())

def div(x, m):
    if m == 0:
        return 1
    elif m == 1:
        return x
    if m % 2 > 0:
        return div(x, m - 1)*x
    half = div(x, m // 2)
    half %= c
    return (half * half) % c

print(div(a, b)%c)

