import sys

sys.stdin = open("input.txt", "r")
ans = 0
while 1:
    try:
        s = input().split(" | ")
        for each in s[1].split():
            if len(each) in [2, 3, 4, 7]:
                ans +=1
    except:break
    
print(ans)

