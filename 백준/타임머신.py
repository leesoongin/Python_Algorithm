

graph = {
    '1':{'2':4,'3':3},
    '2':{'3':-1},
    '3':{'1':-2}
}
graph2 = {
    '1':{'2':4,'3':3},
    '2':{'3':-4},
    '3':{'1':-2}
}
def solution(graph,start):
    distance = dict()

    for node in graph:
        distance[node] = float('inf')
    distance[start] = 0

    for _ in range(len(graph)-1):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]

    for node in graph:
        for neighbour in graph[node]:
            if distance[neighbour] > distance[node] + graph[node][neighbour]:
                return -1
    return distance

print(solution(graph,'1'))
print(solution(graph2,'1'))

# 1 2 4
# 1 3 3
# 2 3 -1
# 3 1 -2

