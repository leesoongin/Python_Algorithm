def solution(graph,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    return graph


graph = [
    [0,1,0],
    [0,0,1],
    [1,0,0]
]

#das
print(solution(graph,3))