from itertools import permutations
import sys

sys.stdin = open("input.txt", "r")
ans = 0
while 1:
    try:
        s = input().split(" | ")
        numbers = {123567: 0, 36: 1, 13457: 2, 13467:3, 2346: 4, 12467: 5, 124567: 6, 136: 7,
                   1234567: 8, 123467: 9}
        def find(word, p):
            indexes = []
            for letter in word:
                indexes += [p.index(ord(letter) - ord('a')) + 1]
            return int("".join(str(k) for k in sorted(indexes)))
        for p in permutations(list(range(7))):
            count = 0
            for each in s[0].split():
                val = find(each, list(p))
                if val in numbers:
                    count += 1
            if count == 10:
                num = ""
                for each in s[1].split():
                    val = find(each, list(p))
                    num += str(numbers[val])
                ans += int(num)
    except:
        break
print(ans)