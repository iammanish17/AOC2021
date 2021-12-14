from collections import defaultdict
from copy import copy
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
present = defaultdict(int)
count = [0] * 26
for i in range(len(s)):
    count[ord(s[i]) - ord('A')] += 1
    if i == len(s) - 1:
        break
    present[(s[i], s[i+1])] += 1
for __ in range(40):
    present_copy = defaultdict(int)
    for x, y in present:
        if (x, y) in pairs:
            z = pairs[(x, y)]
            count[ord(z) - ord('A')] += present[(x, y)]
            present_copy[(x, z)] += present[(x, y)]
            present_copy[(z, y)] += present[(x, y)]
    present = copy(present_copy)
    
ct = sorted(x for x in count if x)
print(ct[-1] - ct[0])