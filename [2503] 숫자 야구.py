from itertools import permutations

def number_baseball(num1, num2):
    strike = 0
    ball = 0

    for i in range(3):
        if num1[i] == num2[i]:
            strike += 1
        else:
            if num1[i] in num2:
                ball += 1

    return strike, ball

if __name__ == "__main__":
    n = int(input())
    answers = [list(map(int, input().strip().split())) for _ in range(n)]
    numbers = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    cnt = 0

    for number in numbers:

        for answer in answers:
            new_answer = [answer[0] // 100, answer[0] // 10 % 10, answer[0] % 100 % 10]
            strike, ball = number_baseball(list(number), new_answer)

            if strike != answer[1] or ball != answer[2]:
                break
        else:
            cnt += 1

    print(cnt)
