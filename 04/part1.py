import sys
sys.stdin = open("input.txt", "r")

numbers = list(map(int, input().split(',')))
boards = []
while 1:
    try:
        blank = input()
        b = []
        for i in range(5):
            b += [list(map(int, input().split()))]
        boards += [b]
    except:break

for x in numbers:
    for k in range(len(boards)):
        found = False
        tot = 0
        for i in range(5):
            for j in range(5):
                if boards[k][i][j] == x:
                    boards[k][i][j] = 0
                    if not sum(boards[k][i]) or not sum(boards[k][y][j] for y in range(5)):
                        found = True
                else:tot += boards[k][i][j]
        if found:
            print(x * tot)
            quit()
