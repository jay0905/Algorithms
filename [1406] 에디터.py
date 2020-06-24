import sys
input = sys.stdin.readline

main_stack = list(input().strip())
sub_stack = []
m = int(input())

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'L':
        if main_stack:
            sub_stack.append(main_stack.pop())
    if cmd[0] == 'D':
        if sub_stack:
            main_stack.append(sub_stack.pop())
    if cmd[0] == 'B':
        if main_stack:
            main_stack.pop()
    if cmd[0] == 'P':
        main_stack.append(cmd[1])

print("".join(main_stack) + "".join(sub_stack[::-1]))
