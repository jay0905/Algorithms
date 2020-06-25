import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
n.sort(reverse=True)

if n[-1] == 0:
    if sum(n) % 3 == 0:
        answer = map(str, n)
        print("".join(answer))
    else:
        print(-1)
else:
    print(-1)
