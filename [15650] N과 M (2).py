n, m = map(int, input().split())
nums = [i+1 for i in range(n)]
checked = [0]*n
outs = []

def dfs(cnt, idx):
    if cnt == m:
        print(*outs)
        return
    for i in range(idx, n):
        if checked[i] == 1:
            continue
        checked[i] = 1
        outs.append(i+1)
        dfs(cnt+1, i+1)
        outs.pop()
        checked[i] = 0

dfs(0, 0)
