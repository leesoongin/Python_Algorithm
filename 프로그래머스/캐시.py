from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    while cities:
        city = cities.pop(0).lower()

        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            if len(q) < cacheSize:
                q.append(city)
                answer += 5
            elif len(q) >= cacheSize:
                q.popleft()
                q.append(city)
                answer += 5

    return answer

# 캐시에 존재하는 경우 + 1
# 존재하지 않을경

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(5,["seoul","seoul","seoul"]))

# 캐시크기(cacheSize)	도시이름(cities)	실행시간
# 3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
# 3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
# 2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
# 5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
# 2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
# 0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25