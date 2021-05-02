from collections import deque

# 0 1 -> 오른쪽
# 0 -1 -> 왼쪽
# 1 0 -> 아래
# -1 0 ->

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())
miro = [list(map(int,input())) for _ in range(n)]

q = deque()
visited = [[False]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]

# 시작 노드를 queue에 넣고 방문처리
q.append((0,0))
visited[0][0] = True
dist[0][0] = 1

while q:
    x,y = q.popleft() # x y 좌표
    #위 아래 양 옆 하나씩 해보리기
    for i in range(len(dx)):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and miro[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
print(dist[-1][-1])









#
#
# from collections import deque
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# n, m = map(int, input().split())
# a = [list(map(int, list(input()))) for _ in range(n)]
# q = deque()
# check = [[False] * m for _ in range(n)]
# dist = [[0] * m for _ in range(n)]
#
# # 시작점
# q.append((0, 0))
# check[0][0] = True
# dist[0][0] = 1
#
# while q:
#     x, y = q.popleft()
#     for k in range(n):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if check[nx][ny] == False and a[nx][ny] == 1:
#                 q.append((nx, ny))
#                 dist[nx][ny] = dist[x][y] + 1
#                 check[nx][ny] = True
#
# print(dist[n - 1][m - 1])