출처: https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dictionary = {}
    answer = []

    for i in range(1, 27):
        dictionary[chr(64 + i)] = i

    check = [True] * (len(msg) + 1)
    for idx, character in enumerate(msg):
        if check[idx] == False:
            continue

        for i in range(idx + 1, len(msg) + 2):
            if i == len(msg) + 1:
                answer.append(dictionary[msg[idx:i]])

            if msg[idx:i] not in dictionary:
                answer.append(dictionary[msg[idx:i-1]])
                dictionary[msg[idx:i]] = len(dictionary) + 1
                break

            for j in range(idx, i):
                check[j] = False

    return answer
