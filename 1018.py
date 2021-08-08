case1 = list('WBWBWBWB')
case2 = list('BWBWBWBW')

inp = input()
inp = inp.split()

n = int(inp[0])
m = int(inp[1])

chess = []

for i in range(n) :
    inp = input()
    chess.append(list(inp))

min_num = 64

for h in range(n-7) :
    for w in range(m-7) :
        current_num = 0
        for i in range(8) :
            for j in range(8) :
                if i%2 == 0 and case1[j] != chess[h+i][w+j] :
                    current_num = current_num+1
                if i%2 == 1 and case2[j] != chess[h+i][w+j] :
                    current_num = current_num+1
        if min_num > current_num :
            min_num = current_num

for h in range(n-7) :
    for w in range(m-7) :
        current_num = 0
        for i in range(8) :
            for j in range(8) :
                if i%2 == 0 and case2[j] != chess[h+i][w+j] :
                    current_num = current_num+1
                if i%2 == 1 and case1[j] != chess[h+i][w+j] :
                    current_num = current_num+1
        if min_num > current_num :
            min_num = current_num

print(min_num)
