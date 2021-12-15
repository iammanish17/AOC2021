import sys

sys.stdin = open("input.txt", "r")
a = []
while 1:
    try:
        s = list(map(int, list(input())))
        a += [s]
    except:
        break
n = len(a)
m = len(a[0])

a = [[a[i][j] if (i < n and j < m) else 0 for j in range(5*m)] for i in range(5*n)]
for i in range(5*n):
    for j in range(5*m):
        if i < n and j < m: continue
        a[i][j] = ((a[i % n][j % m] + (i // n) + (j // m) - 1) % 9) + 1

n*=5
m*=5

from heapq import heappop, heappush

distance = [[float("inf")] * m for _ in range(n)]
distance[0][0] = 0
parents = [[-1] * m for _ in range(n)]
queue = []
heappush(queue, (0, 0, 0))
while queue:
    length, x, y = heappop(queue)
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if distance[nx][ny] > distance[x][y] + a[nx][ny]:
                distance[nx][ny] = distance[x][y] + a[nx][ny]
                parents[nx][ny] = (x, y)
                heappush(queue, (distance[nx][ny], nx, ny))
print(distance[-1][-1])