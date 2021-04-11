#역순으로 정렬

def solution(arr):
    answer = list()

    answer = sorted(arr,reverse=True)

    print(answer)
    return answer

solution([3,15,27,12])