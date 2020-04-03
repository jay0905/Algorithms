import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())
map = [list(input().strip()) for _ in range(R)]

for i in range(R):
    map[i].insert(0, '.')
    map[i].append('.')

map.insert(0, ['.' for _ in range(C + 2)])
map.append(['.' for _ in range(C + 2)])

def not_sink(map, i, j):
    cnt = 0
    if i >= 1 and j >= 1:
        if map[i - 1][j] == 'X':
            cnt += 1
        if map[i + 1][j] == 'X':
            cnt += 1
        if map[i][j - 1] == 'X':
            cnt += 1
        if map[i][j + 1] == 'X':
            cnt += 1

    return True if cnt >= 2 else False

new_map = []

for i in range(1, R + 1):
    row = []
    for j in range(1, C + 1):
        if map[i][j] == 'X' and not_sink(map, i, j):
            row.append('X')
        else:
            row.append('.')
    new_map.append(row)

row_minimum = column_minimum = 11
row_maximum = column_maximum = 0

for i in range(len(new_map)):
    for j in range(len(new_map[i])):
        if new_map[i][j] == 'X':
            row_minimum = min(i, row_minimum)
            row_maximum = max(i, row_maximum)
            column_minimum = min(j, column_minimum)
            column_maximum = max(j, column_maximum)

result_map = []

if row_minimum == 11 and column_minimum == 11 and row_maximum == 0 and column_maximum == 0:
    row_minimum = column_minimum = 0
    row_maximum = len(new_map) - 1
    column_maximum = len(new_map[0]) - 1

for i in range(row_minimum, row_maximum + 1):
    row = []
    for j in range(column_minimum, column_maximum + 1):
        row.append(new_map[i][j])
    result_map.append(row)

for i in range(len(result_map)):
    print(''.join(result_map[i]))
