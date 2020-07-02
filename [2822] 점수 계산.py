import sys
input = sys.stdin.readline

scores = []
for i in range(1, 9):
    score = int(input())
    scores.append((score, i))

scores.sort(reverse=True)
five_scores = []
scores_sum = 0

for i in range(5):
    five_scores.append(scores[i][1])
    scores_sum += scores[i][0]

print(scores_sum)
five_scores.sort()
for i in range(5):
    print(five_scores[i], end=" ")
