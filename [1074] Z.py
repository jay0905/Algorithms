import sys
input = sys.stdin.readline

def draw_z(n, x, y):
    global cnt

    if n == 1:
        if (x, y) != (r, c) and (x, y + 1) != (r, c) and (x + 1, y) != (r, c) and (x + 1, y + 1) != (r, c):
            cnt += 4
        else:
            if (x, y + 1) == (r, c):
                cnt += 1
            if (x + 1, y) == (r, c):
                cnt += 2
            if (x + 1, y + 1) == (r, c):
                cnt += 3

            print(cnt)
            return
    else:
        draw_z(n - 1, x, y)
        draw_z(n - 1, x, y + 2**(n - 1))
        draw_z(n - 1, x + 2**(n - 1), y)
        draw_z(n - 1, x + 2**(n - 1), y + 2**(n - 1))

n, r, c = map(int, input().split())
cnt = 0

draw_z(n, 0, 0)
