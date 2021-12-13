import sys

sys.stdin = open("input.txt", "r")
points = []
while 1:
    s = input()
    if s == "":
        break
    x, y = map(int, s.split(','))
    points += [(x, y)]

for times in range(1):
    inst = input().split()[-1]
    val = int(inst.split('=')[-1])
    if inst.startswith('x'):
        points = list(set([(x, y) if x <= val else (2*val - x, y) for x, y in points]))
    else:
        points = list(set([(x, y) if y <= val else (x, 2*val - y) for x, y in points]))

print(len(points))
print(points)