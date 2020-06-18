import sys
input = sys.stdin.readline

A = []
N, M = map(int, input().split())

for _ in range(N):
    A.append(list(map(int, input().split())))

B = []
M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

answer = [[0] * K for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            answer[n][k] += A[n][m] * B[m][k]

for row in answer:
    for num in row:
        print(num, end=' ')
    print()
