from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
city = [list(map(int, input().strip().split())) for _ in range(n)]
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))

chicken_combi = list(combinations(chicken, m))
distances = []

for combi in chicken_combi:
    new_city = list(map(list, city))

    for i in range(n):
        for j in range(n):
            if new_city[i][j] == 2 and (i, j) not in combi:
                new_city[i][j] = 0

    distance = 0
    houses = []
    chicken_place = []
    for i in range(n):
        for j in range(n):
            if new_city[i][j] == 1:
                houses.append((i, j))
            if new_city[i][j] == 2:
                chicken_place.append((i, j))

    for house in houses:
        MINIMUM = 999
        for place in chicken_place:
            MINIMUM = min(MINIMUM, abs(house[0] - place[0]) + abs(house[1] - place[1]))

        distance += MINIMUM

    distances.append(distance)

print(min(distances))
