# N은 노드의 개수
# M은 간선의 개수
# V는 첫번째 정점

N,M,V = map(int,input().split())

matrix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

visited = [False]*(N+1)

def dfs(V):
    visited[V] = True
    print(V,end = '')
    # 방문하지않은 다른 연결된 노드도 방문하기
    for i in range(N+1):
        if matrix[V][i] == 1 and visited[i] == False:
            dfs(i)

def bfs(V):
    queue = [V]
    visited[V] = False
    while queue:
        v= queue.pop(0)
        print(v,end='')
        for i in range(N+1):
            if visited[i] and matrix[V][i]:
                queue.append(i)
                visited[i] = False


dfs(V)
print('\n')
bfs(V)