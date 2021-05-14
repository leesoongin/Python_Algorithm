def solution(arr, divisor):
    answer = []
    test = 1

    for item in arr:
        if item % divisor == 0:
            answer.append(item)
    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)


# 지린다 ㄹㅇ,,
# or은 앞에꺼가 참이라면 실행되지않고 거짓이라면 뒤까지 실행됨
def solution(arr, divisor):
    return sorted([item for item in arr if item % divisor == 0]) or [-1]

print(solution([3,2,6],10))