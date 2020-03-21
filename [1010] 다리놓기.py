import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())
    cnt = 1

    for i in range(m, m-n, -1):
        cnt *= i
    for i in range(n, 0, -1):
        cnt //= i

    print(cnt)
