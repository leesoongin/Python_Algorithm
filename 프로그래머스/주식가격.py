from collections import deque
prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    queue=deque(prices)
    while queue:
        v=queue.popleft()
        count = 0
        for i in queue:
            if v<=i:
                count+=1
            else:
                count+=1
                break
        answer.append(count)
    return answer


print(solution(prices))