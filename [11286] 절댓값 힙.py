import heapq, sys
input = sys.stdin.readline

n = int(input())

my_list = []
heapq.heapify(my_list)

for _ in range(n):
    x = int(input())

    if x == 0:
        if my_list:
            answer = heapq.heappop(my_list)
            print(answer[1])
        else:
            print(0)
    else:
        heapq.heappush(my_list, (abs(x), x))
