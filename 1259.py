while True :
    inp = input()
    if inp == '0' :
        break

    k = True
    
    for i, a in enumerate(inp) :
        if a != inp[len(inp)-i-1] :
            print('no')
            k = False
            break

    if k :
        print('yes')
