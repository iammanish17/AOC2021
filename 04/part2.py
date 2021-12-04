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
    except:
        break

pos = [True]*len(boards)
for x in numbers:
    for k in range(len(boards)):
        if not pos[k]: continue
        found = False
        tot = 0
        pt = False
        for i in range(5):
            for j in range(5):
                if boards[k][i][j] == x:
                    boards[k][i][j] = 0
                    if not sum(boards[k][i]) or not sum(boards[k][y][j] for y in range(5)):
                        found = True
                        pos[k] = False
                        if sum(pos) == 0:pt = True
                else:
                    tot += boards[k][i][j]
        if pt:
            print(x * tot)
            quit()
