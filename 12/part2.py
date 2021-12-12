import sys

sys.stdin = open("input.txt", "r")

graph = [[] for __ in range(1000)]
di = {}
di2 = {}
while 1:
    try:
        x, y = list(map(str, input().split('-')))
        if x not in di:
            di[x] = len(di)
            di2[len(di) - 1] = x
        if y not in di:
            di[y] = len(di)
            di2[len(di) - 1] = y
        graph[di[x]].append(di[y])
        graph[di[y]].append(di[x])
    except:
        break

st, en = di["start"], di["end"]


def f(cur, vis=None):
    if cur == en:
        return 1
    ans = 0
    for x in graph[cur]:
        if not di2[x].lower() == di2[x]:
            ans += f(x, list(vis) + [x])
        else:
            if di2[x] in ['start', 'end']:
                if x not in vis:
                    ans += f(x, list(vis) + [x])
                continue
            pos = 1
            for y in vis:
                if di2[y].lower() == di2[y] and vis.count(y) > 1:
                    pos -= 1
                    break
            if pos == 1 or vis.count(x) == 0:
                ans += f(x, list(vis) + [x])
    return ans


print(f(st, list([st])))