with open("01/input.txt", "r") as f:
    data = f.read()
    f.close()
    
data = data.split("\n")

x = None
ans = 0
for each in data:
    each = int(each)
    if x is None:
        x = each
    else:
        if each > x:
            ans += 1
        x = each
print(ans)

x = []
ans = 0
for each in data:
    each = int(each)
    if len(x) < 3:
        x += [each]
        continue
    total = sum(x)
    x.pop(0)
    x += [each]
    if sum(x) > total:
        ans += 1
print(ans)