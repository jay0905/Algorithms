출처: https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):

    seperated = []

    for file in files:

        DIGIT = False
        num_start = 0
        num_end = len(file)

        for idx, s in enumerate(file):
            if s.isdigit() and DIGIT is False:
                DIGIT = True
                num_start = idx

            elif not s.isdigit() and DIGIT is True:
                num_end = idx
                break

        seperated.append([file, file[:num_start].lower(), int(file[num_start:num_end]), file[num_end + 1:].lower()])

    seperated.sort(key=lambda x : (x[1], x[2]))
    answer = []
    
    for i in range(len(seperated)):
        answer.append(seperated[i][0])

    return answer
