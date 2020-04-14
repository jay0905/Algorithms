from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
answers = input().strip().split()
student_answers = input().strip().split()

answer_dict = {}
for idx, answer in enumerate(answers):
    answer_dict[answer] = idx

answer_idx = []
for answer in student_answers:
    answer_idx.append(answer_dict[answer])

two_answer = list(combinations(answer_idx, 2))

correct = 0
for first, second in two_answer:
    if first < second:
        correct += 1

print(str(correct) + "/" + str(len(two_answer)))
