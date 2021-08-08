inp = input()
inp = int(inp)

ans = 0
count = 0

while True :
    temp = str(ans)
    if "666" in temp :
        count = count+1
    if count == inp :
        print(ans)
        break
    ans = ans+1
