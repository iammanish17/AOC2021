import sys

sys.stdin = open("input.txt", "r")

s = input()
blank = input()
a = []
while 1:
    try:
        line = input()
        a += [list('.' * 5000 + line + '.' * 5000)]
    except EOFError:
        break
for i in range(5000):
    a = ['.' * len(a[-1])] + a + ['.' * len(a[-1])]
n, m = len(a), len(a[0])
for times in range(50):
    print("Running: ",times, flush=True)
    b = [[''] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            val = 256 * (a[(i - 1) % n][(j - 1) % m] == '#') + \
                  128 * (a[(i - 1) % n][j] == '#') + \
                  64 * (a[(i - 1) % n][(j + 1) % m] == '#') + \
                  32 * (a[i][(j - 1) % m] == '#') + \
                  16 * (a[i][j] == '#') + \
                  8 * (a[i][(j + 1) % m] == '#') + \
                  4 * (a[(i + 1) % n][(j - 1) % m] == '#') + \
                  2 * (a[(i + 1) % n][j] == '#') + \
                  1 * (a[(i + 1) % n][(j + 1) % m] == '#')
            b[i][j] = s[val]
    a = [list(x) for x in b]
print(sum(x.count("#") for x in a))