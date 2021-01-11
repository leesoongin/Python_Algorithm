
def solution(priorities, location):
    answer = 0
    paperList=[]
    resultList=[]

    for index,value in enumerate(priorities):
        if index == location:
            paperList.append(Paper(value,True))
        else:
            paperList.append(Paper(value,False))

    while paperList:
        popItem = paperList.pop(0)
        isCheck = False
        for i in paperList:
            if i.priorities > popItem.priorities:
                paperList.append(popItem)
                isCheck = True
                break
        if isCheck == False:
            resultList.append(popItem)

    for i in resultList:
        if i.bool :
            answer=resultList.index(i)+1
    return answer


class Paper:
    def __init__(self,priorities,bool):
        self.priorities = priorities
        self.bool = bool
    def __lt__(self, other):
        return self.priorities > other.priorities

priorities=[2, 1, 3, 2]
location=2

print(solution(priorities,location))
