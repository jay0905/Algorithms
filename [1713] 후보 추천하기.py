import sys
input = sys.stdin.readline

n = int(input())
all = int(input())
recomendations = list(map(int, input().strip().split()))
frame = []

for idx, num in enumerate(recomendations):

    for i in range(len(frame)):
        if frame[i][0] == num:
            frame[i][2] += 1
            break
    else:
        if len(frame) >= n:
            frame.pop()

        frame.append([num, idx, 1])

    frame.sort(key= lambda x:(x[2], x[1]), reverse=True)

answer = [frame[i][0] for i in range(len(frame))]
answer.sort()

print(*answer)
