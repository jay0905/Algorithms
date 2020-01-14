n, m = map(int, input().split())
nums = [i+1 for i in range(n)]
checked = [0]*n
outs = []

def dfs(cnt):
    if cnt == m: # m의 개수만큼 채워지면 출력
        print(*outs)
        return
    for i in range(n):
        if checked[i] == 1: # 이미 방문했으면 생략
            continue
        checked[i] = 1 # 이제 방문하므로
        outs.append(i+1) # 수열 원소 추가
        dfs(cnt+1)
        outs.pop()
        checked[i] = 0 # 다음 방문할 곳으로 넘어가기 전에 초기화를 시켜준다

dfs(0)
