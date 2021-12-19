import sys
sys.stdin = open("input.txt", "r")
data = sys.stdin.read()

a = []

for s in data.split("\n\n"):
    a += [[]]
    for point in s.split("\n")[1:]:
        x, y, z = map(int, point.split(","))
        a[-1] += [(x, y, z)]
        
def get_permutations(x, y, z):
    ans = []
    for p, q, r in [(x, y, z), (y, z, x), (z, x, y), (x, z, y), (y, x, z), (z, y, x)]:
        ans += [(p, q, r), (-p, q, r), (p, -q, r), (-p, -q, r), (p, q, -r), (-p, q, -r), (p, -q, -r), (-p, -q, -r)]
    return ans

current = set(a[0])
a.pop(0)
    
left = True
while left:
    left = False
    for i in range(len(a)):
        def check(i):
            for j in range(48):
                for x, y, z in current:
                    for x2, y2, z2 in a[i]:
                        x2, y2, z2 = get_permutations(x2, y2, z2)[j]
                        offx, offy, offz = x2-x, y2-y, z2-z
                        newset = set()
                        finalset = set()
                        for xb, yb, zb in a[i]:
                            xbb, ybb, zbb = get_permutations(xb, yb, zb)[j]
                            finalset.add((xbb-offx, ybb-offy, zbb-offz))
                            if (xbb-offx, ybb-offy, zbb-offz) in current:
                                newset.add((xb, yb, zb))
                        if len(newset) >= 12:
                            return finalset
            return None
        cc = check(i)
        if cc:
            a.pop(i)
            left = True
            current |= cc
            print("Found match, new length: ", len(current), flush=True)
            break
print(len(current))