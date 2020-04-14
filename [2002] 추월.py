import sys
input = sys.stdin.readline

n = int(input())
start = [input().strip() for _ in range(n)]
end = [input().strip() for _ in range(n)]
start_idx = dict()
end_idx = []

for idx, car in enumerate(start):
    start_idx[car] = idx

for car in end:
    end_idx.append(start_idx[car])

checked = [0] * n
answer = 0
for idx in end_idx:
    if idx == 0:
        checked[idx] = 1
    else:
        for i in range(idx):
            if checked[i] == 0:
                answer += 1
                break
        checked[idx] = 1

print(answer)
