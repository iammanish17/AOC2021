with open("input.txt", "r") as f:
    data = f.read()
    f.close()
data = data.split("\n")
count = [0]*len(data[0])
for each in data:
    for x in range(len(each)):
        count[x] += int(each[x])

p = ''
q = ''
for x in count:
    if 2 * x > len(data):
        p += '1'
        q += '0'
    else:
        p += '0'
        q += '1'

print(int(p,2)*int(q,2))