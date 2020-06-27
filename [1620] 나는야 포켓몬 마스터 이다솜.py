import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
monsters_num = dict()
monsters_name = dict()

for i in range(1, n + 1):
    name = input().strip()
    monsters_num[i] = name
    monsters_name[name] = i

for _ in range(m):
    question = input().strip()

    if question.isdigit():
        print(monsters_num[int(question)])
    else:
        print(monsters_name[question])
