def solution(cacheSize, cities):
    answer = 0
    cache = list()

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache: # hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: # miss
            if len(cache) < cacheSize: # 정상
                cache.append(city)
                answer += 5
            else:
                cache.pop(0)
                cache.append(city)
                answer += 5

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

# 캐시크기(cacheSize)	도시이름(cities)	실행시간
# 3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
# 3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
# 2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
# 5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
# 2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
# 0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25

#LRU 알고리즘 사용
# 캐시에 원히는게 존재하지 않을경우 가장 마지막으로 사용된녀석을 제외한다. (주의점!!) 이미 존재하는 녀석이 들어온다면 그녀석을 제거하고 다시 가장 최근으로 돌려줘야한다.
# 그럼,, 일단 가장 마지막 녀석이 나갈거니까  queue를 사용하자.
# 다시 들오온녀석은 일단 제거하거 가장 마지막 부분에 추가하자.