def solution(graph):
    answer = 0

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                graph[i][j] = min(graph[i][k]+graph[k][j],graph[i][j])
    print(graph)
    return answer

INF = float('inf')
graph = [
    [0,5,INF,8],
    [7,0,9,INF],
    [2,INF,0,4],
    [INF,INF,3,0]
]

print(solution(graph))