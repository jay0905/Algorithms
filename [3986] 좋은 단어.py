import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
cnt = 0

for word in words:
    fixed_word = ""

    stack = []
    for alphabet in word:
        if not stack:
            stack.append(alphabet)
        else:
            if stack[-1] == alphabet:
                stack.pop()
            else:
                stack.append(alphabet)
    else:
        if not stack:
            cnt += 1

print(cnt)
