with open("input.txt", "r") as f:
    data = f.read()
    f.close()
data = data.split("\n")
h = 0
aim = 0
dp = 0
for each in data:
    x, y = each.split()
    y = int(y)
    if x == "forward":
        h += y
        dp += y * aim
    if x == "down":
        aim += y
    if x == "up":
        aim -= y

print(h * dp)