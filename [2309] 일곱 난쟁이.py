from itertools import combinations

heights = [int(input()) for _ in range(9)]
combi = list(combinations(heights, 7))

for c in combi:
    if sum(c) == 100:
        answer = c
        break

answer = list(c)
answer.sort()

for one in answer:
    print(one)
