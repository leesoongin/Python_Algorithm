from collections import deque
import copy
def solution(progresses,speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while(progresses):
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for progress,speed in zip(progresses.copy(),speeds.copy()):
            if progress >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            else:
                break
        if count:
            answer.append(count)

    return answer


print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]



# def solution(progresses, speeds):
#     answer = []
#     resultList = deque(progresses)
#     speeds = deque(speeds)
#     while resultList:
#         count=0
#         for i in range(len(resultList)):
#             resultList[i]+=speeds[i]
#         for i in range(len(resultList)):
#             if resultList[i] >= 100:
#                 count+=1
#             else:
#                 break
#
#         for i in range(count):
#             resultList.popleft()
#             speeds.popleft()
#
#         if count > 0:
#             answer.append(count)
#
#     return answer
#
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
#
# print(solution(progresses,speeds))


