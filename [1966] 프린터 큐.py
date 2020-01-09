t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))
    ans = [0]*n
    ans[m] = 'T'
    cnt = 0
    while True:
        if que[0] == max(que):
            cnt += 1
            if ans[0] == 'T':
                break
            else:
                que.pop(0)
                ans.pop(0)
        else:
            que.append(que.pop(0))
            ans.append(ans.pop(0))
    print(cnt)
