# 출처: https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    arr1_to_bin = []
    arr2_to_bin = []

    for num1, num2 in zip(arr1, arr2):
        num1_to_bin = bin(num1)[2:]
        num2_to_bin = bin(num2)[2:]
        
        if len(num1_to_bin) < n:
            num1_to_bin = (n - len(num1_to_bin)) * "0" + num1_to_bin

        if len(num2_to_bin) < n:
            num2_to_bin = (n - len(num2_to_bin)) * "0" + num2_to_bin
            
        arr1_to_bin.append(num1_to_bin)
        arr2_to_bin.append(num2_to_bin)

    answer = []
    for i in range(n):
        row = ""

        for bin1, bin2 in zip(arr1_to_bin[i], arr2_to_bin[i]):
            if bin1 == "0" and bin2 == "0":
                row += " "
            else:
                row += "#"

        answer.append(row)

    return answer
