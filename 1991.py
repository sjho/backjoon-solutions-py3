n = int(input())

tree = []

for _ in range(n) :
    tree.append([])
    for _ in range(2) :
        tree[-1].append(-1)

base = ord('A')

for _ in range(n) :
    inp = input().split(' ')
    i = ord(inp[0])-base
    for j, n in enumerate(inp[1:]) :
        if n != '.' :
            tree[i][j] = ord(n)-base

def left_search(num):
    left = tree[num][0]
    right = tree[num][1]

    print(chr(num+base), end='')
    if left >= 0 :
        left_search(left)
    if right >= 0 :
        left_search(right)

def middle_search(num):
    left = tree[num][0]
    right = tree[num][1]

    if left >= 0 :
        middle_search(left)
    print(chr(num+base), end='')
    if right >= 0 :
        middle_search(right)

def right_search(num):
    left = tree[num][0]
    right = tree[num][1]

    if left >= 0 :
        right_search(left)
    if right >= 0 :
        right_search(right)
    print(chr(num+base), end='')

left_search(0)
print()
middle_search(0)
print()
right_search(0)
print()