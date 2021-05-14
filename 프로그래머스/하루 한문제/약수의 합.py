def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)

    return sum(answer)

def solution2(n):
    return sum([i for i in range(1,n+1) if n % i == 0])

print(solution(12))
print(solution(5))
print(solution2(12))
print(solution2(5))
# n	return
# 12	28
# 5	6