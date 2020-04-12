import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
triangle = [[0], [1], [1, 1]]

for i in range(3, n + 1):
    for j in range(i):
        if j == 0:
            triangle.append([1])
        elif j == i - 1:
            triangle[i].append(1)
        else:
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

print(triangle[n][k - 1])
