arr = [7,5,9,0,3,1,6,2,4,8]

def solution(array):
    answer = list()

    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    answer = array
    print(answer)

    return answer

solution(arr)