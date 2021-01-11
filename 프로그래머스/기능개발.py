from collections import deque

def solution(progresses, speeds):
    answer = []
    resultList = deque(progresses)
    speeds = deque(speeds)
    while resultList:
        count=0
        for i in range(len(resultList)):
            resultList[i]+=speeds[i]
        print(resultList)
        for i in range(len(resultList)):
            if resultList[i] >= 100:
                count+=1
            else:
                break

        for i in range(count):
            resultList.popleft()
            speeds.popleft()

        if count > 0:
            answer.append(count)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses,speeds))