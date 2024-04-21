import sys
input = sys.stdin.readline
arr = [list(map(int, input().strip())) for _ in range(9)]
zeroSpaces = []


for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zeroSpaces.append((i, j))
n = len(zeroSpaces)


def checkPossible(r, c, num):
    for i in range(9):
        if arr[r][i] == num:
            return False
        if arr[i][c] == num:
            return False

    startR, startC = (r//3)*3, (c//3)*3

    for i in range(startR, startR+3):
        for j in range(startC, startC+3):
            if arr[i][j] == num:
                return False
    return True


def backtracking(count):
    if n == count:
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end="")
            print()
        exit()

    nowR, nowC = zeroSpaces[count]
    for i in range(1, 10):
        if checkPossible(nowR, nowC, i):
            arr[nowR][nowC] = i
            backtracking(count+1)
            arr[nowR][nowC] = 0


backtracking(0)
print()


"""
유망함수 = 세로 가로 줄 + 안에 3x3 판단 

"""
