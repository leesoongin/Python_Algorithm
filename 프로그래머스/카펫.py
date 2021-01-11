

def solution(brown,yellow):
    answer=[]
    yellowCase=div(yaksu(yellow))
    # 가로개수+2*2 + 세로개수*2 = brown이면  true / true일떄 yellocase의 가로세로 각각 +2씩한게 결과값
    if yellow == 1:
        answer.append(yellow+2)
        answer.append(yellow+2)
    else:
        for case in yellowCase:
            if brown == ((case[0]+2)*2)+((case[1])*2):
                answer.append(case[0]+2)
                answer.append(case[1]+2)

    return answer

def yaksu(num): # 여기 들어갈 수는 yellow로 하
    yaksuList=[]
    for i in range(1,num+1):
        if num%i == 0:
            yaksuList.append(i)

    return list(reversed(yaksuList))

def div(yaksuList):
    divList=[]

    if (len(yaksuList))%2 == 0: # 약수의 개수가 짝수일때.
        for i in range(len(yaksuList)//2):
            couple = []
            couple.append(yaksuList[i])
            couple.append(yaksuList[-(i+1)])
            divList.append(couple)
    else: # ex 4 의 약수  1 2 4 인경우.   약수의 개수가 홀수일때
        while len(yaksuList) > 0:
            couple=[]

            if len(yaksuList) >= 2:
                couple.append(yaksuList.pop(0))
                couple.append(yaksuList.pop())
                divList.append(couple)
            else:
                couple.append(yaksuList[0]); couple.append(yaksuList.pop())
                divList.append(couple)

    return divList

print(yaksu(36))
print(div(yaksu(36)))

print(solution(8,1))
