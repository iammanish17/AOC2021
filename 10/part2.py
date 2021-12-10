import sys

sys.stdin = open("input.txt", "r")
ans = []
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
        pos = True
        for x in s:
            if x in '({<[':
                q += [x]
            else:
                if not q:
                    pos = False
                    break
                if x != '<>{}()[]'['<>{}()[]'.index(q.pop()) + 1]:
                    pos = False
                    break
        if pos:
            val = 0
            while q:
                val = val * 5 + 1 + '([{<'.index(q.pop())
            ans += [val]
    except:
        break
print(sorted(ans)[len(ans) // 2])