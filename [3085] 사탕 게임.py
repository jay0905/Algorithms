def continuity_cnt_row(n, candies):
    cnt_temp = []

    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if candies[i][j] == candies[i][j + 1]:
                cnt += 1
            else:
                cnt_temp.append(cnt)
                cnt = 1

        cnt_temp.append(cnt)

    cnt_temp.sort()
    return cnt_temp[-1]

def continuity_cnt_column(n, candies):
    cnt_temp = []

    for j in range(n):
        cnt = 1
        for i in range(n - 1):
            if candies[i][j] == candies[i + 1][j]:
                cnt += 1
            else:
                cnt_temp.append(cnt)
                cnt = 1

        cnt_temp.append(cnt)

    cnt_temp.sort()
    return cnt_temp[-1]

n = int(input())
candies = [list(input()) for _ in range(n)]
candidates = []

for i in range(n):
    for j in range(n - 1):
        temp = candies[i][j]
        candies[i][j] = candies[i][j + 1]
        candies[i][j + 1] = temp

        candidates.append(continuity_cnt_row(n, candies))
        candidates.append(continuity_cnt_column(n, candies))

        candies[i][j + 1] = candies[i][j]
        candies[i][j] = temp

for j in range(n):
    for i in range(n - 1):
        temp = candies[i][j]
        candies[i][j] = candies[i + 1][j]
        candies[i + 1][j] = temp

        candidates.append(continuity_cnt_row(n, candies))
        candidates.append(continuity_cnt_column(n, candies))

        candies[i + 1][j] = candies[i][j]
        candies[i][j] = temp

candidates.sort()
print(candidates[-1])
