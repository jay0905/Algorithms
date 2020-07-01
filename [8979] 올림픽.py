import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medals = []

for _ in range(n):
    number, gold, silver, bronze = map(int, input().split())
    medals.append([gold, silver, bronze, number])

medals.sort(reverse=True)
rankings = [1]

for i in range(n):

    same_cnt = 0

    if i != 0:
        if medals[i][0] == medals[i - 1][0] and medals[i][1] == medals[i - 1][1] and medals[i][2] == medals[i - 1][2]:
            rankings.append(rankings[-1])
        else:
            rankings.append(i + 1)

    if medals[i][3] == k:
        print(rankings[-1])
        break
