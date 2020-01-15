n, m = map(int, input().split())
nums = [i+1 for i in range(n)]
outs = []

def dfs(cnt, idx):
    if cnt == m:
        print(*outs)
        return
    for i in range(idx, n):
        outs.append(i+1)
        dfs(cnt+1, i)
        outs.pop()

dfs(0, 0)
