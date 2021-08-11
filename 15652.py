n, m = map(int, input().split())

def result(i, l) :
    for j in range(i, n+1) :
        temp = l.copy()
        temp = temp + [j]

        if len(temp) >= m :
            for t in temp :
                print(t, end=' ')
            print()
        else :
            result(j, temp)
    

result(1, [])