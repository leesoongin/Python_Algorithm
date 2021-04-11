

def solution(arr):
    answer = 0

    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j] , arr[j-1] = arr[j-1], arr[j]
            else :
                break

    answer = arr
    print(answer)
    return answer


array = [7,5,9,0,1,3,6,2,4,8]

solution(array)

#거의 정렬된 상태에서