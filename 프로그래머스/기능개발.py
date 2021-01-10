
def solution(progresses, speeds):
    answer = []
    result=[0 for _ in range(len(progresses))]

    while result:
        count=0
        for index,value in enumerate(zip(progresses,speeds)):
            result[index]+=value[0]+value[1]
        for i in result:
            if i >=100:
                count+=1
                progresses.pop(0); speeds.pop(0); result.pop(0)

        if count != 0:
            answer.append(count)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses,speeds))