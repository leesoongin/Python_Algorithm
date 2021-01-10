from itertools import cycle

def solution(answers):
    count = [0,0,0]
    answer = []

    supo1=[1,2,3,4,5]
    supo2=[2,1,2,3,2,4,2,5]
    supo3=[3,3,1,1,2,2,4,4,5,5]

    for one,two,three,num in zip(cycle(supo1),cycle(supo2),cycle(supo3),answers):
        if one == num:
            count[0]+=1
        if two == num:
            count[1]+=1
        if three == num:
            count[2]+=1

    for index,value in enumerate(count):
        if value == max(count):
            answer.append(index+1)

    return answer

answers=[1,3,2,4,2]

print(solution(answers))