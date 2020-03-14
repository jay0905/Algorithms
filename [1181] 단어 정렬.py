import sys, collections
input = sys.stdin.readline

n = int(input())

vocas = list(set([input().strip() for _ in range(n)]))
vocas.sort(key=lambda x: (len(x), x))

for voca in vocas:
    print(voca)
