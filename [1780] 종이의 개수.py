import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

minus = 0
zero = 0
plus = 0

def cut(x, y, n):
    global minus, zero, plus
    check = matrix[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != matrix[i][j]:
                for k in range(3):
                    for l in range(3):
                        cut(x + k*(n // 3), y + l*(n // 3), n // 3)
                return

    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        plus += 1
    return

cut(0, 0, n)
print(minus, zero, plus, sep='\n')
