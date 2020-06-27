import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for num in range(1, n + 1):
    if num % 5 == 0:
        while num % 5 != 0:
            num /= 5
            cnt += 1

print(cnt)
