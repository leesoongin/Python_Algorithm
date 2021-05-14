def solution(a, b):
    answer = 0
    numlist = sorted([a,b])

    for i in range(numlist[0],numlist[1]+1):
        answer += i
    return answer


# 0 ~ n 까지의 합을 sum안의 range로 해버렸네 range(3,6)으로 나옴 이거 자체를 더하기하면 그 범위의 숫자를 더할 수 있느듯 개쩐다
def solution2(a,b):
    if a>b :
        a,b = b,a
    return sum(range(a,b+1))
print(solution2(3,5))

# a	b	return
# 3	5	12
# 3	3	3
# 5	3	12