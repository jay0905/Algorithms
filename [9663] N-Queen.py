n = int(input())
ans = 0
# 세로, 대각선(/), 대각선(\)
arr1, arr2, arr3 = [0]*n, [0]*(2*n-1), [0]*(2*n-1)

def nqueen(x): # x는 현재 행
    global ans
    if x == n: # n개의 행에 퀸을 하나씩 둬야 하므로, x가 n이 되었다면 퀸을 다 둔 것
        ans += 1
        return
    for i in range(n):
        if arr1[i] or arr2[x+i] or arr3[x-i+n-1]: # 열이나 대각선에 이미 퀸이 놓아져있다면 그 경우는 생략
            continue
        arr1[i] = arr2[x+i] = arr3[x-i+n-1] = 1
        nqueen(x+1)
        arr1[i] = arr2[x+i] = arr3[x-i+n-1] = 0

nqueen(0)
print(ans)
    
