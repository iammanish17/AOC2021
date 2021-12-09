import sys

sys.stdin = open("input.txt", "r")
ans = 0
a = []
while 1:
    try:
        s = [int(k) for k in input()]
        a += [s]
    except:break

n, m = len(a), len(a[0])
for i in range(n):
    for j in range(m):
        mi = float("inf")
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m:
                mi = min(mi, a[x][y])
        if a[i][j] < mi:
            ans += a[i][j] + 1
print(ans)