
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.


# 4,5,1
# 5,5,3


# n : 정점의 개수 , m: 간선의 개수 start: 시작 노
def bfs(graph,start):
    visited = list()
    queue = list()
    queue.append(start)
    visited.append(start)

    while queue:
        node = queue.pop(0)
        for item in graph[node]:
            if item not in visited:
                visited.append(item)
                queue.append(item)
    print(visited)
    return

def dfs(graph,start,visited):
    visited.append(start)
    print(start,end=' ')

    for node in graph[start]:
        if node not in visited:
            dfs(graph,node,visited)
    return

n,m,start = map(int,input().split())
graph = [
    [],
    [2,3],
    [1,5],
    [1,4],
    [3,5],
    [2,4]
]
dfs(graph,start,[])
bfs(graph,start)