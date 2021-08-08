inp = input()
inp = input()

ans = 0
l = 0
for i in inp :
    ans = ans + (ord(i)-ord('a')+1)*pow(31, l)
    l = l+1

ans = ans % 1234567891
print(ans)
