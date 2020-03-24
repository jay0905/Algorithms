def solution(board):
    if len(board) == 1:
        if 1 in board[0]:
            return 1
        return 0
    
    maximum = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
            maximum = max(board[i][j], maximum)

    return maximum ** 2
