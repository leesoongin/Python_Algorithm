from collections import deque


def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])

    q = deque()
    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = True
    dist[0][0] = 1

    while q:
        x, y = q.popleft()  # x y 좌표
        # 위 아래 양 옆 하나씩 해보리기
        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and maps[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    if nx == n - 1 and ny == m - 1 and dist[nx][ny] != 1:
                        return dist[-1][-1]
    return -1
    # return -1 if len(answer) == 0 else min(answer)


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

# maps	answer
# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1