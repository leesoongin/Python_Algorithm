# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 왼 오 아래
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(n,m,graph):
    queue = list()
    count = -1
    # 처음 익은 토마토들을 queue에 넣자
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                queue.append((i,j))
    while queue:
        count += 1

        # 처음 익은 토마토가 여러개인 경우, 여러군데에서 토마톼 익어가기 때문에옴
        # 하루가 지날때에 queue에 있는 토마토 녀석들의 주변을 싹 탐색하며 count해야 제대로 된 일수가 나
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0<=nx<m) and (0<=ny<n) and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

    for item in graph:
        if 0 in item:
            return -1
    return count



graph = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,1],
]

print(bfs(6,4,graph))