import sys
input = sys.stdin.readline

n = int(input())
times = [list((map(int, input().strip().split()))) for _ in range(n)]
times.sort(key=lambda x: [x[1], x[0]])

end_time = 0
cnt = 0

for x, y in times:
    if x >= end_time:
        cnt += 1
        end_time = y

print(cnt)
