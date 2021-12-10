import sys

sys.stdin = open("input.txt", "r")
ans = 0
while 1:
    try:
        s = input()
        q = []
        points = {
            ')': 3,
            ']': 57,
            '>': 25137,
            '}': 1197
        }
        for x in s:
            if x in '({<[':
                q += [x]
            else:
                if not q:
                    ans += points[x]
                    break
                if x != '<>{}()[]'['<>{}()[]'.index(q.pop()) + 1]:
                    ans += points[x]
                    break
    except:
        break
print(ans)