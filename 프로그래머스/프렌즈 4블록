import numpy as np

def solution(m, n, board):
    answer = 0
    map = list()
    for item in board:
        tmp = []
        for ele in item:
            tmp.append(ele)
        map.append(tmp)
    board = map

    while True:
        if checkExist(board,m,n) == False: # 더이상 겹치는게 존재하지 않는다면.
            break
        checkPoint = findCheckPoint(board,m,n)
        board = delBlock(board,checkPoint)        
        board = dropBlock(board,m,n)
    
    for item in board:
        answer += item.count(" ")
    
    return answer

def checkExist(board,m,n):
    for i in range(1,m):
        for j in range(1,n):
            if board[i][j-1] == board[i][j] and board[i-1][j-1] == board[i][j] and board[i-1][j] == board[i][j] and board[i][j] != " ":
                return True
    return False

def findCheckPoint(board,m,n):
    checkPoint = list()
    for i in range(1,m):
        for j in range(1,n):
            if board[i][j-1] == board[i][j] and board[i-1][j-1] == board[i][j] and board[i-1][j] == board[i][j]:
                checkPoint.append([i,j,board[i][j]])
    return checkPoint

def delBlock(board,checkPoint):
    for i,j,block in checkPoint:
        board[i][j] = board[i][j].replace(block," ")
        board[i][j-1] = board[i][j-1].replace(block," ")
        board[i-1][j] = board[i-1][j].replace(block," ")
        board[i-1][j-1] = board[i-1][j-1].replace(block," ")
    return board

def dropBlock(board,m,n):
    rows = list()
    
    for j in range(n):
        tmp = []
        for i in range(m):
            if not board[i][j] == " ":
                tmp.append(board[i][j])
        while len(tmp) < m:
            tmp.insert(0," ")
        rows.append(tmp)
    
    return np.transpose(rows).tolist()

            
        

# 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)
