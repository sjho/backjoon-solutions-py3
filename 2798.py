inp = input()
inp = inp.split()
m = int(inp[1])

inp = input()
nums = inp.split()

ans = 0

for i in range(len(nums)) :
    for j in range(i+1, len(nums)) :
        for k in range(j+1, len(nums)) :
            temp = int(nums[i])+int(nums[j])+int(nums[k])
            if abs(m-temp) < abs(m-ans) and temp <= m :
                ans = temp


print(ans)
