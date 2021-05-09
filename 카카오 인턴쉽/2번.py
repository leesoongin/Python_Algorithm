# 예외 파티션이 존재하는 경우, 거리가 2 이하인 경  5x5
from collections import deque
# [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#  ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
#  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def solution(places):
    answer = []
    # 5개의 강의실을 만들고 , bfs를 각각ㄱ의 강의실마다 돌리고, return값을 1 or 0으로 하면 되겠다. 토마토랑 똑같은 문

    for place in places:
        placesList = list()

        for index,item in enumerate(place):
            placesList.append(list(map(str,item)))
        print(bfs(placesList))
    return answer


def bfs(graph):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    queue = list()
    registList = list()
    #탐색할친구 queue에 추
    for i,item in enumerate(graph):
        for j,element in enumerate(item):
            if element == 'P':
                queue.append([i,j])


    # 숫자로 변환
    for i,item in enumerate(graph):
        for j,element in enumerate(item):
            if element == 'X':
                graph[i][j] = -1
            elif element == 'P':
                graph[i][j] = 1
            else:
                graph[i][j] = 0
    print(graph)
    while queue:
        for _ in range(len(queue)):
            x,y = queue.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < 5) and (0 <= ny < 5) and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx,ny])
                if (0 <= nx < 5) and (0 <= ny < 5) and graph[nx][ny] == 1:
                    registList.append((nx,ny))
    registList = set(registList)
    registList = list(registList)

    for i in range(len(registList)):
        for j in range(i+1,len(registList)):
            if abs(registList[i][0] - registList[j][0]) + abs(registList[i][1] - registList[j][1]) <= 2:
                print(registList[i],registList[j])
                return 0

    return 1


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
