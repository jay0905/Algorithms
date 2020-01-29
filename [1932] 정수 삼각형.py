import sys
input = sys.stdin.readline

n = int(input())
tri = []

for _ in range(n):
    tri.append(list(map(int, input().strip().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tri[i][0] += tri[i-1][0]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])

print(max(tri[n-1]))
