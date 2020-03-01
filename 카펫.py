def solution(brown, red):
    answer = []
    MINIMUM = 3
    MAXIMUM = 2497

    for height in range(MINIMUM, MAXIMUM):
        for width in range(height, MAXIMUM):
            if brown == 2*width + 2*height - 4:
                if red == width*height - 2*width - 2*height + 4:
                    answer.append(width)
                    answer.append(height)
                    return answer
