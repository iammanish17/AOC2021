import sys

sys.stdin = open("input.txt", "r")

a = list(map(int, input().split(",")))
val = 10 ** 9
for i in range(min(a), max(a) + 1):
    ans = 0
    for j in a:
        t = abs(i - j)
        ans += (t * (t + 1)) // 2
    val = min(val, ans)
print(val)