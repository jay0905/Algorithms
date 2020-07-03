import sys
input = sys.stdin.readline

red_green = ["R", "G"]
def check_weakness_color(x, y, nx, ny, n, colors, section_red_green):
    return 0 <= nx < n and 0 <= ny < n and ((colors[x][y] in red_green and colors[nx][ny] in red_green) or colors[x][y] == colors[nx][ny]) and section_red_green[nx][ny] == 0

def check_same_color(x, y, nx, ny, n, colors, section_normal):
    return 0 <= nx < n and 0 <= ny < n and colors[x][y] == colors[nx][ny] and section_normal[nx][ny] == 0

def fill_same_colors(weakness, i, j, n, colors, normal_color_number, section_normal):
    stack = [(i, j)]
    section_normal[i][j] = normal_color_number

    while stack:
        x, y = stack.pop()

        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy

            # 색약이면
            if weakness:
                if check_weakness_color(x, y, nx, ny, n, colors, section_red_green):
                    section_red_green[nx][ny] = red_green_number
                    stack.append((nx, ny))
            # 색약이 아니면
            else:
                if check_same_color(x, y, nx, ny, n, colors, section_normal):
                    section_normal[nx][ny] = normal_color_number
                    stack.append((nx, ny))

n = int(input())
colors = [list(input().strip()) for _ in range(n)]

section_normal = [[0] * n for _ in range(n)]
normal_color_number = 0

for i in range(n):
    for j in range(n):
        if section_normal[i][j] == 0:
            normal_color_number += 1
            fill_same_colors(False, i, j, n, colors, normal_color_number, section_normal)

section_red_green = [[0] * n for _ in range(n)]
red_green_number = 0

for i in range(n):
    for j in range(n):
        if section_red_green[i][j] == 0:
            red_green_number += 1
            fill_same_colors(True, i, j, n, colors, red_green_number, section_red_green)

print(normal_color_number, red_green_number)
