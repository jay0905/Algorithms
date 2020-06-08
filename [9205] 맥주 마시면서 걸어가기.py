import sys
input = sys.stdin.readline
INF = sys.maxsize

for _ in range(int(input())):
    n = int(input())

    maps = [[INF] * (n + 2) for _ in range(n + 2)]
    locations = []

    for _ in range(n + 2):
        x, y = map(int, input().split())
        locations.append((x, y))

    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue

            dist = abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])
            if dist <= 1000:
                maps[i][j] = 1
                maps[j][i] = 1

    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if i == j:
                    maps[i][j] = 0
                else:
                    maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])

    print("happy" if maps[0][n + 1] != INF else "sad")
