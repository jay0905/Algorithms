def solution(record):
    splitted_record = []
    id_nickname = {}
    result = []
    
    for r in record:
        rr = r.split(" ")
        if rr[0] == "Enter" or rr[0] == "Change":
            id_nickname[rr[1]] = rr[2]
            
    for r in record:
        rr = r.split(" ")
        if rr[0] == "Enter":
            result.append(id_nickname[rr[1]] + "님이 들어왔습니다.")
        elif rr[0] == "Leave":
            result.append(id_nickname[rr[1]] + "님이 나갔습니다.")

    return result
