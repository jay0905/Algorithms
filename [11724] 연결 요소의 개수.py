import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(v):
    VISITED[v] = True

    for e in adj[v]:
        if not VISITED[e]:
            dfs(e)

n, m = map(int, input().strip().split())
adj = [[] for _ in range(n + 1)]
VISITED = [False] * (n + 1)
cnt = 0

for _ in range(m):
    connected = list(map(int, input().strip().split()))
    adj[connected[0]].append(connected[1])
    adj[connected[1]].append(connected[0])

for i in range(1, len(VISITED)):
    if not VISITED[i]:
        cnt += 1
        dfs(i)

print(cnt)
