import sys

sys.stdin = open("input.txt", "r")

def get_sum(s, i = 0):
    version = int(s[i:(i+3)], 2)
    type_id = int(s[(i+3):(i+6)], 2)
    if type_id == 4:
        i += 6
        while s[i] == '1':
            i += 5
        return i + 4, version
    length_type = int(s[i+6])
    if length_type == 0:
        sub_length = int(s[(i+7):(i+7+15)], 2)
        i += 7 + 15
        j = i
        ans = version
        while j != i + sub_length:
            j, val = get_sum(s, j)
            j += 1
            ans += val
        return j - 1, ans
    else:
        sub_count = int(s[(i+7):(i+7+11)], 2)
        i += 7 + 11
        j = i
        ans = version
        while sub_count:
            sub_count -= 1
            j, val = get_sum(s, j)
            j += 1
            ans += val
        return j - 1, ans

def make4(s):
    return "0" * (4 - len(s)) + s
s = "".join(make4(bin(int(x, 16))[2:]) for x in input())
finish_index, total = get_sum(s)
print(total)