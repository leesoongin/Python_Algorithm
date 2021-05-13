def solution(arr):
    answer = []

    for item in arr:
        if len(answer) == 0:
            answer.append(item)
        elif answer[-1] != item:
            answer.append(item)

    return answer


def solution(arr):
    answer = []
    
    for item in arr:
        if len(answer) == 0:
            answer.append(item)
        elif answer[-1] != item:
            answer.append(item)

    return answer


print(solution([1,1,3,3,0,1,1]))
# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]
