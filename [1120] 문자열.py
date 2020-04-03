import sys
input = sys.stdin.readline

A, B = input().strip().split()
max_cnt = 0

for i in range(len(B) - len(A) + 1):
    part_B = B[i:i+len(A)]
    cnt = 0

    for a, b in zip(A, part_B):
        if a == b:
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(len(A) - max_cnt)
