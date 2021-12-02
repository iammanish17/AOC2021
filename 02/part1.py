with open("input.txt", "r") as f:
    data = f.read()
    f.close()
data = data.split("\n")
h = 0
dp = 0
for each in data:
    x, y = each.split()
    y = int(y)
    if x == "forward":
        h += y
    if x == "down":
        dp += y
    if x == "up":
        dp -= y
        
print(h*dp)