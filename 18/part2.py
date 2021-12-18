import sys

sys.stdin = open("input.txt", "r")


def combine(x, y):
    x = ['['] + x + [','] + y + [']']
    for i in range(len(x)):
        if type(x[i]) == int or x[i].isdigit(): x[i] = int(x[i])
    changes = True
    while changes:
        changes = False
        open = 0
        for i in range(len(x)):
            if x[i] == '[':
                open += 1
                if open == 5:
                    j = i - 1
                    while j >= 0:
                        if type(x[j]) == int:
                            x[j] += x[i + 1]
                            break
                        j -= 1
                    j = i + 5
                    while j < len(x):
                        if type(x[j]) == int:
                            x[j] += x[i + 3]
                            break
                        j += 1
                    x = x[:i] + [0] + x[(i + 5):]
                    changes = True
                    break
            if x[i] == ']':
                open -= 1
        if not changes:
            for i in range(len(x)):
                if type(x[i]) == int and x[i] >= 10:
                    changes = True
                    x = x[:i] + ['[', x[i] // 2, ',', (x[i] + 1) // 2, ']'] + x[i + 1:]
                    break
    return x


def magnitude(x):
    if len(x) == 1:
        return x[0]
    open = 0
    for i in range(len(x)):
        if x[i] == '[': open += 1
        if x[i] == ']': open -= 1
        if open == 1 and x[i] == ',':
            return 3 * magnitude(x[1:i]) + 2 * magnitude(x[i + 1:-1])


numbers = []
while 1:
    try:
        s = input()
        numbers += [list(s)]
    except EOFError:
        break

ans = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        ans = max(ans, magnitude(combine(list(numbers[i]), list(numbers[j]))))
print(ans)