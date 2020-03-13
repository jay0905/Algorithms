import sys
input = sys.stdin.readline

expressions = input().strip().split('-')
numbers = []

for expression in expressions:
    num_sum = 0
    splitted_nums = expression.split('+')

    for num in splitted_nums:
        num_sum += int(num)

    numbers.append(num_sum)

answer = numbers[0]
for i in range(1, len(numbers)):
    answer -= numbers[i]

print(answer)
