with open("input.txt", "r") as f:
    data = f.read()
    f.close()
data = data.split("\n")
data2 = list(data)
for i in range(len(data[0])):
    p = [[], []]
    for k in data:
        p[int(k[i])] += [k]
    if len(p[0]) > len(p[1]):
        data = list(p[0])
    else:
        data = list(p[1])
ans1 = data[0]
data = list(data2)
for i in range(len(data[0])):
    if len(data) == 1: break
    p = [[], []]
    for k in data:
        p[int(k[i])] += [k]
    if len(p[0]) <= len(p[1]):
        data = list(p[0])
    else:
        data = list(p[1])
ans2 = data[0]
print(int(ans1,2)*int(ans2,2))