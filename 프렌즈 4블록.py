def solution(m, n, board):
    
    modified = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    answer = 0
    
    while True:
        delete = set()

        for i in range(n - 1):
            for j in range(len(modified[i]) - 1):
                
                if j >= len(modified[i + 1]) - 1: 
                    break
                    
                if modified[i][j] == modified[i + 1][j] == modified[i][j + 1] == modified[i + 1][j + 1]:
                    delete.add((i, j))
                    delete.add((i + 1, j))
                    delete.add((i, j + 1))
                    delete.add((i + 1, j + 1))

        for x, y in reversed(sorted(delete)):
            modified[x].pop(y)
            
        if len(delete) == 0:
            break
            
        answer += len(delete)

    return answer
