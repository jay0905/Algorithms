import sys, math
input = sys.stdin.readline

n = int(input())
n_length = len(str(n))
answer = 0

for i in range(n_length - 1):
    answer += 9 * (10 ** i) * (i + 1)

answer += (int(n) - (10 ** (n_length - 1)) + 1) * n_length

print(answer)
