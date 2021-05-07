
def binarySearch(arr,target):
    leftIndex = 0  # 탐색할 배열의 시작 인덱스
    rightIndex = len(arr)-1  # 탐색할 배열의 마지막 인덱스

    # 가장 최악의 경우, 배열의 크기가 1이 되므로 leftIndex >= rightIndex 혹은 leftIndex == rightIndex가 종료조건
    while leftIndex <= rightIndex:
        middle = (leftIndex + rightIndex) // 2

        if target < arr[middle]:
            rightIndex = middle - 1
        elif target > arr[middle]:
            leftIndex = middle + 1
        else:
            return arr[middle] # or middle

    # 만약 while문이 종료된다면 탐색하는 값이 존재하지 않으므로 -1일단 return함
    return -1




print(binarySearch([1,2,3,5,6,7,9,10,11,13,14,15,16,17,20,21],13))



