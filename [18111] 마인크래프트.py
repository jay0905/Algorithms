import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, b = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(n)]
height_cnt = [0] * 257

for i in range(n):
    for j in range(m):
        height_cnt[heights[i][j]] += 1

min_height = 256
max_height = 0

for row in heights:
    min_height = min(min_height, min(row))
    max_height = max(max_height, max(row))

candidates = []
for current_height in range(min_height, max_height + 1):
    time = 0
    block_cnt = b

    for i in range(min_height, max_height + 1):

        if height_cnt[i]:
            if current_height > i:
                time += (current_height - i) * height_cnt[i]
                block_cnt -= (current_height - i) * height_cnt[i]
            elif current_height < i:
                time += (i - current_height) * height_cnt[i] * 2
                block_cnt += (i - current_height) * height_cnt[i]

    if block_cnt >= 0:
        candidates.append((time, current_height))

candidates.sort(key=lambda x:(x[0], -x[1]))
print(candidates[0][0], candidates[0][1])
