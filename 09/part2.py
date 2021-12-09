import sys

sys.stdin = open("input.txt", "r")
ans = 0
a = []
while 1:
    try:
        s = [int(k) for k in input()]
        a += [s]
    except:
        break

n, m = len(a), len(a[0])
graph = [[] for i in range(n*m + 1)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 9:continue
        mi = float("inf")
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and a[x][y] != 9:
               graph[i*m + j + 1] += [x*m + y + 1]
               graph[x*m+y+1] += [i*m + j + 1]


def connected_components(n, graph):
    components, visited = [], [False] * n
    
    def dfs(start):
        component, stack = [], [start]
        
        while stack:
            start = stack[-1]
            
            if visited[start]:
                stack.pop()
                continue
            else:
                visited[start] = True
                component.append(start)
            
            for i in graph[start]:
                if not visited[i]:
                    stack.append(i)
        
        return component
    
    for i in range(n):
        if not visited[i]:
            components.append(dfs(i))
    
    return components

comp = connected_components(n*m+1, graph)
def product(a):
    ans = 1
    for each in a:
        ans *= each
    return ans
print(product(sorted([len(x) for x in comp])[-3:]))