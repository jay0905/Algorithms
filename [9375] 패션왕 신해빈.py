import collections, sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = []

    for _ in range(n):
        clothes.append(input().strip().split()[1])

    clothes_counter = collections.Counter(clothes)
    dict(clothes_counter)

    ans = 1
    for key in clothes_counter:
        ans *= clothes_counter[key] + 1

    print(ans - 1)
