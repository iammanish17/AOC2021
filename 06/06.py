import sys

sys.stdin = open("input.txt", "r")

a = list(map(int, input().split(",")))
count = [0] * 9
for x in a:
    count[x] += 1
for i in range(256):
    x = count[0]
    count = [count[i+1] for i in range(8)]
    count += [0]
    count[6] += x
    count[8] += x
    if i+1 == 80:print("Part 1:", sum(count))
print("Part 2:", sum(count))