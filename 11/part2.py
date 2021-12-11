import sys

sys.stdin = open("input.txt", "r")

a = []
for i in range(10):
    a += [list(int(k) for k in input())]
_ = 0
while 1:
    pos = False
    for i in range(10):
        for j in range(10):
            a[i][j] += 1
            pos |= (a[i][j] > 9)
    
    while pos:
        b = [[0] * 10 for __ in range(10)]
        pos = False
        for i in range(10):
            for j in range(10):
                if a[i][j] > 9:
                    continue
                if a[i][j] == 0: continue
                flag = False
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == dy == 0: continue
                        if 0 <= i + dx < 10 and 0 <= j + dy < 10 and a[i + dx][j + dy] > 9:
                            flag += 1
                b[i][j] = a[i][j] + flag
                pos |= (b[i][j] > 9)
        for i in range(10):
            a[i] = list(b[i])
    if not sum(sum(a[i]) for i in range(10)):
        print(_ + 1)
        quit()
    _ += 1