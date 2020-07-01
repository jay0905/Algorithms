import sys
input = sys.stdin.readline

letters = [list(input().strip()) for _ in range(5)]
answer = ""

for i in range(15):
    for letter in letters:
        if len(letter) > i:
            answer += letter[i]

print(answer)
