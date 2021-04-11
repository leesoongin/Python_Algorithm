def solution(arr):
    answer = 0

    # for i in range(len(arr)):
    #     for j in range(len(arr)-1,i,-1):
    #         if arr[j-1] > arr[j]:
    #             arr[j-1], arr[j] = arr[j], arr[j-1]

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    answer = arr
    print(answer)

    return answer



array = [3,1,4,5,2]

solution(array)