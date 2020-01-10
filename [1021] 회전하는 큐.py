import sys

n, m = map(int, sys.stdin.readline().strip().split())
que = [i+1 for i in range(n)]
num = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

while num:
    if num[0] == que[0]:
        del que[0]
        del num[0]
    elif que.index(num[0]) > len(que) / 2:
        while num[0] != que[0]:
            que.insert(0, que.pop())
            cnt += 1
    elif que.index(num[0]) <= len(que) / 2:
        while num[0] != que[0]:
            que.append(que.pop(0))
            cnt += 1

print(cnt)
