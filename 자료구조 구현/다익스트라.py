import heapq # 우선순위 큐 마냥 사용할수 있는 녀석
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
graph2 = [
    [],
    [(3,6),(4,3)],
    [(1,3)],
    [(4,2)],
    [(2,1),(3,1)],
    [(2,4),(4,2)]
]
import heapq  # 우선순위 큐 구현을 위함


def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[start,distances[start]])

    while queue:
        current_node,current_distance = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
        for child_node,child_distance in graph[current_node].items():
            if distances[child_node] > child_distance:
                distances[child_node] = child_distance
                heapq.heappush(child_node,distances[child_node])
    return


def dijkstra2(graph,start):
    q = []
    distances = [ float('inf') for _ in range(len(graph))] # 시작노드를 제외하고 나머지는 전부 가장 큰 값으로 초기화한다.
    heapq.heappush(q,(0,start))
    distances[start] = 0 # 시작노드에서 시작노드로 가는 가중치는 0

    while q:
        # 큐에 있는 노드들 중, 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        # heapq 라이브러라는 최소 힙 자료구조로 구현되어 있음. 그래서 값이 작을수록 우선순위가 높아 pop하면 가장 작은 가중치를 가진 노드의 정보가 나옴
        distance, current_node = heapq.heappop(q)

        if distances[current_node] < distance : #  distances의 초기값은 시작노드를 제외하고 무한대.
            continue
        for i in graph[current_node]:
            new_distance = distance + i[1] # 현재 노드에 연결된 노드로부터 인접해 있는 노드에 방문
            if new_distance < distances[i[0]]: #  (이때, 나의 가중치 + 인접노드로의 가중치 와 최소가중치 리스트의 값과 비교)
                distances[i[0]] = new_distance # 값 다시 설정
                heapq.heappush(q,(new_distance,i[0])) # 인접노드 queue에 저장

    for i in range(1, len(graph2)):
        print(i,distances[i])
    return

dijkstra2(graph2,5)


# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함 // 결과적으로 모든 최단거리 저장함
#     distances[start] = 0
#     queue = [] # 방문한 녀석들 처리하려고 사용
#     heapq.heappush(queue,[distances[start],start]) # 시작 노드로부터 목적지 노드로까지의 거리, 목적지 노드
#
#     while queue:
#         curDistance, curDestination = heapq.heappop(queue)
#         if distances[curDestination] < curDistance: # queue에 저장되어 있는 거리보다  지금 계산한 거리가 더 크다면 그냥 지나감
#             continue
#         for newDestination, newDistance in graph[curDestination].items():
#             distance = curDistance + newDistance
#             if distances[newDestination] > distance:
#                 distances[newDestination] = distance
#                 heapq.heappush(queue,[distance,newDestination])
#
#     return distances


# print(dijkstra(graph,'A'))
