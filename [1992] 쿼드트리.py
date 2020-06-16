import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int, input().strip())) for _ in range(n)]
answer = []

def compress(x, y, n):
    check = video[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != video[i][j]:
                answer.append("(")
                compress(x, y, n // 2)
                compress(x, y + n // 2, n // 2)
                compress(x + n // 2, y, n //2)
                compress(x + n // 2, y + n // 2, n // 2)
                answer.append(")")
                return

    answer.append(str(video[x][y]))
    return

compress(0, 0, n)
print("".join(answer))
