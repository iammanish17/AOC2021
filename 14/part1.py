import sys

sys.stdin = open("input.txt", "r")

s = input()
blank = input()
pairs = {}
while 1:
    try:
        x, y = input().split(" -> ")
        pairs[(x[0], x[1])] = y
    except:
        break
s = list(s)
for __ in range(10):
    t = []
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            t += [s[i]]
            break
        if (s[i], s[i+1]) in pairs:
            t += [s[i], pairs[(s[i], s[i+1])]]
            i += 1
        else:
            t += [s[i]]
            i += 1
    s = list(t)
ct = sorted(list(set([s.count(k) for k in set(s)])))
print(ct[-1] - ct[0])