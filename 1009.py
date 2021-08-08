inp = input()
t = int(inp)

p = [[10],
     [1],
     [6, 2, 4, 8],
     [1, 3, 9, 7],
     [6, 4],
     [5],
     [6],
     [1, 7, 9, 3],
     [6, 8, 4, 2],
     [1, 9]]

for i in range(t) :
    inp = input()
    inp = inp.split()

    a = int(inp[0])
    b = int(inp[1])

    print(p[(a%10)][(b%len(p[(a%10)]))])

    

    
