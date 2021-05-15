def solution(left, right):
    answer = 0

    for num in range(left,right+1):
        count = 0
        for i in range(1,num+1):
            if num % i ==0:
                count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer

# 1/2 제곱해서(루트) 완전히 나누어 떨어지는 수라면 약수의 개수가 홀수개, 완전히 나누어 떨어지지 않는다면 약수의 개수는 짝수개.
def solution2(left, right):
    answer = 0
    for num in range(left,right+1):
        if num**0.5 == int(num**0.5):
            answer -= num
        else:
            answer += num

    return answer

# print(solution(13,17))
# print(solution(1,1))

print(solution2(16,16))
# print(solution2(1,1))
# left	right	result
# 13	17	43
# 24	27	52