def solution(N,stages):
    userDict = dict()
    userCount = len(stages)

    for i in range(1,N+1):
        if userCount == 0:
            userDict[i] = 0
        else:
            count = stages.count(i)
            userDict[i] = count / userCount
            userCount -= count

    return sorted(userDict,key=lambda x: -userDict[x])

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4,[4,4,4,4,4]))
# 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	[4,4,4,4,4]	[4,1,2,3] -> 현재 멈춰있는 스테이지임,
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수


#
# def solution(N, stages):
#     arr = []
#     answer = []
#     clearUsers = dict()
#     arriveUsers = dict()
#     resultUsers = dict()
#
#     for i in range(1,N+1):
#         clearUsers[i] = 0
#     for i in range(1,N+1):
#         arriveUsers[i] = 0
#     for i in range(1, N + 1):
#         resultUsers[i] = 0
#     # 클리어한 수
#     for item in stages:
#         for i in range(1,item):
#             clearUsers[i] += 1
#     # 도달한 수
#     for item in stages:
#         for i in range(1,item+1):
#             if i == N+1 :
#                 continue
#             else:
#                 arriveUsers[i] += 1
#     # 도달한 수 - 클리어한 수 = 도달했으니 클리어하지 못한 수
#     for i in range(1,len(clearUsers)+1):
#         resultUsers[i] = arriveUsers[i] - clearUsers[i]
#
#     for i in range(1,len(clearUsers)+1):
#         if arriveUsers[i] == 0:
#             arr.append([i,0])
#         else:
#             arr.append([i,resultUsers[i]/arriveUsers[i]])
#     arr = sorted(arr,key=lambda x :(-x[1] , x[0]))
#
#     for item in arr:
#         answer.append(item[0])
#     return answer