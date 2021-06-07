from collections import deque

def solution(priorities,location):
    answer = 0
    queue = deque([[index,item] for index,item in enumerate(priorities)])
    while True:
        current = queue.popleft()
        if any(current[1] < item[1] for item in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer


print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))

# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
# def solution(priorities, location):
#     answer = 0
#     paperList=[]
#     resultList=[]
#
#     for index,value in enumerate(priorities):
#         if index == location:
#             paperList.append(Paper(value,True))
#         else:
#             paperList.append(Paper(value,False))
#
#     while paperList:
#         popItem = paperList.pop(0)
#         isCheck = False
#         for i in paperList:
#             if i.priorities > popItem.priorities:
#                 paperList.append(popItem)
#                 isCheck = True
#                 break
#         if isCheck == False:
#             resultList.append(popItem)
#
#     for i in resultList:
#         if i.bool :
#             answer=resultList.index(i)+1
#     return answer
#
#
# class Paper:
#     def __init__(self,priorities,bool):
#         self.priorities = priorities
#         self.bool = bool
#     def __lt__(self, other):
#         return self.priorities > other.priorities
#
# priorities=[2, 1, 3, 2]
# location=2
#
# print(solution(priorities,location))
