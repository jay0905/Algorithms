import sys
input = sys.stdin.readline

n, k = map(int, input().split())
events = [[0] * n for _ in range(n)]

for _ in range(k):
    before, after = map(int, input().split())
    events[before - 1][after - 1] = 1

for l in range(n):
    for i in range(n):
        for j in range(n):
            if events[i][j] == 1 or (events[i][l] == 1 and events[l][j] == 1):
                events[i][j] = 1

s = int(input())
for _ in range(s):
    e1, e2 = map(int, input().split())

    if events[e1 - 1][e2 - 1]:
        print(-1)
    elif events[e2 - 1][e1 - 1]:
        print(1)
    else:
        print(0)
