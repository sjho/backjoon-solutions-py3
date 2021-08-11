inp = list(map(int, input().split(' ')))

n = int(inp[0])
m = int(inp[1])

def result(start, stack) :
    for i in range(start+1, n+1) :
        if len(stack) < m-1 :
            result(i, stack+[i])
        else :
            for j in stack+[i] :
                print(j, end=' ')
            print()

result(0, [])