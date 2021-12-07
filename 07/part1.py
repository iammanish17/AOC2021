import sys

sys.stdin = open("input.txt", "r")

a = list(map(int, input().split(",")))
val = 10**9
for i in a:
    ans = 0
    for j in a:
        ans += abs(i-j)
    val = min(val, ans)
print(val)