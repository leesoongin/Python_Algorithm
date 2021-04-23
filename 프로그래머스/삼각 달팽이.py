# 이차원배열사용

# 예) size ->  [1][1]
# [2][2] [3][3]

# def solution(n):
#     answer = []
#
#     snailList = [[0 for _ in range(i+1)] for i in range(n)]
#     number = 1
#     x = 0
#     for y in range(n):
#
#         snailList[y][x] = number
#         number += 1
#     return answer


def solution(n):
    answer = []

    snailList = [[0 for _ in range(i+1)] for i in range(n)]
    x = 0; y = -1
    number = 1
    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1; y -= 1
            snailList[y][x] = number
            number += 1
    for item in snailList:
        for innerItem in item:
            answer.append(innerItem)
    return answer

solution(6)
