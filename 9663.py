n = int(input())

def queen_chk(chess, x) :
    for i in range(x) :
        if chess[i] == chess[x] or x-i == abs(chess[i]-chess[x]):
            return False
    return True

chess = []

for i in range(n) :
    chess.append(0)

def n_queen(x, c) :
    count = c
    if x == n :
        return count + 1
    else :
        for i in range(n) :
            temp = 0
            chess[x] = i
            if queen_chk(chess, x) :
                temp = temp + n_queen(x+1, temp)
            count = count + temp
        return count

print(n_queen(0, 0))