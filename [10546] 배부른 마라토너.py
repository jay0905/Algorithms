import sys
input = sys.stdin.readline

n = int(input())
participants = [input().strip() for _ in range(n)]
succeed = [input().strip() for _ in range(n - 1)]

participants.sort()
succeed.sort()

for p, s in zip(participants, succeed):
    if p != s:
        print(p)
        break
else:
    print(participants[-1])
