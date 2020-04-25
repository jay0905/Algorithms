# 출처: https://programmers.co.kr/learn/courses/30/lessons/43237

def solution(budgets, M):
    budgets.sort()
    start = 1
    end = budgets[-1]
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        budgets_sum = 0
        for budget in budgets:
            budgets_sum += min(budget, mid)
            
        if budgets_sum <= M:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer
