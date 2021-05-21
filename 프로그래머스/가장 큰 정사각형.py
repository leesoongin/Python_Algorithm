def solution(board):
    answer = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1],board[i-1][j],board[i-1][j-1]) + 1
    for i in board :
        answer = max(max(i),answer)
    return answer **2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))



