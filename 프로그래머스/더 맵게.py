import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if K == 0:
        return 0
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        answer += 1
        one,two = heapq.heappop(scoville) , heapq.heappop(scoville)
        heapq.heappush(scoville,one+two*2)
    return answer if scoville[0] >= K else -1

print(solution([1, 2, 3, 9, 10, 12],7))
print(solution([9],7))
print(solution([0,0,0,0,0,0],7))
# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2