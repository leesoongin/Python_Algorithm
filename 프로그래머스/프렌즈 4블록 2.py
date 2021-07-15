import numpy as np


def solution(m, n, board):
    answer = 0
    checkPoint = list()
    map = list()

    for item in board:
        tmp = []
        for ele in item:
            tmp.append(ele)
        map.append(tmp)

    while isExistCheckPoint(m, n, map):  # 지워질게 존재하는동안 while
        checkPoint = findCheckPoint(m, n, map)  # 찾기
        map = delElement(map, checkPoint)  # 지우기
        map = downElement(m, n, map)  # 내리기

    # 이걸 더이상 checkPoint가 안찾아질때까지 돌리면 되겠따! ㅋㅅㅋ
    for item in map:
        answer += item.count(" ")

    return answer


def isExistCheckPoint(m, n, map):
    for i in range(1, m):
        for j in range(1, n):
            if map[i][j] == map[i][j - 1] and map[i][j] == map[i - 1][j - 1] and map[i][j] == map[i - 1][j] and map[i][
                j] != " ":
                return True
    return False


def findCheckPoint(m, n, map):
    checkPoint = list()
    for i in range(1, m):
        for j in range(1, n):
            if map[i][j] == map[i][j - 1] and map[i][j] == map[i - 1][j - 1] and map[i][j] == map[i - 1][
                j]:  # 왼, 왼위, 위 같다면
                checkPoint.append([i, j, map[i][j]])
    return checkPoint


def delElement(map, checkPoint):
    # 지우는걸 공백처리를 할까? ㅇㅇ 그러자
    for i, j, ele in checkPoint:
        map[i][j] = " "
        map[i][j - 1] = " "
        map[i - 1][j - 1] = " "
        map[i - 1][j] = " "

    return map


# 내리기
def downElement(m, n, map):
    cList = list()

    # 빈 공간 붙이고 앞에 공백 추가한다음 행, 열 change하면 될듯
    for j in range(n):
        tmp = []
        for i in range(m):
            if map[i][j] == " ":  # 빈 공간 붙임
                continue
            tmp.append(map[i][j])
        while len(tmp) < m:  # 공백 추가
            tmp.insert(0, " ")
        cList.append(tmp)

    # 행열 추가 numpy 쓰자 근데 기억안남 ㅋㅋㅅㅋ 어케하더라
    map = np.transpose(cList).tolist()

    return map

    # 찾고
    # 지우고
    # 내리고
    # 반벅