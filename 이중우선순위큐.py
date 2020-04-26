import heapq

def solution(operations):
    answer = []
    numbers = []

    for operation in operations:
        cmd = operation.split()[0]
        data = operation.split()[1]

        if cmd == "I":
            heapq.heappush(numbers, int(data))
        else:
            if not numbers:
                continue
                
            if data == "-1":
                heapq.heappop(numbers)
            else:
                numbers = [-number for number in numbers]
                heapq.heapify(numbers)
                
                heapq.heappop(numbers)
                
                numbers = [-number for number in numbers]
                heapq.heapify(numbers)

    if numbers:
        answer.append(heapq.heappop(numbers))
        
        numbers = [-number for number in numbers]
        heapq.heapify(numbers)

        answer.append(-heapq.heappop(numbers))
        answer.sort(reverse=True)

        return answer

    return [0,0]
