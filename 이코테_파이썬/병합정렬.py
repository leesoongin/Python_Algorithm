def solution(array):
    answer = marge_sort(arr)
    print(answer)
    return answer

def marge_sort(unsortedList):
    if len(unsortedList) <= 1:
        return unsortedList

    mid = len(unsortedList)//2
    leftArr = unsortedList[:mid]
    rightArr = unsortedList[mid:]

    divideLeftArr = marge_sort(leftArr)
    divideRightArr = marge_sort(rightArr)
    # 다 나눈 뒤 마지막 돌아올때 합치면서
    return marge(divideLeftArr,divideRightArr)

def marge(leftArr,rightArr):
    i =0; j=0
    sortedList = list()

    while i < len(leftArr) and j < len(rightArr):
        # 각 arr의 가장 작은값들끼리의 비교. 두 배열중 하나의 배열이 다 들어갈때 까지
        if leftArr[i] < rightArr[j]:
            sortedList.append(leftArr[i])
            i += 1
        else:
            sortedList.append(rightArr[j])
            j += 1
        # 만약 아직까지 sortedList에 들어가지 않고 남아있는 배열이 존재한다면, 남은거 다 넣어주
    while i < len(leftArr):
        sortedList.append(leftArr[i])
        i += 1
    while j < len(rightArr):
        sortedList.append(rightArr[j])
        j += 1

    return sortedList



arr = [1,3,2,5,4,6,8,7]
solution(arr)


