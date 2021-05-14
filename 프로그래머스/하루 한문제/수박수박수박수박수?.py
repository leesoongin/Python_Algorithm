def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer

def solution2(n):
    return '수박'*(n//2)+'수'*(n%2)

print(solution(3))
print(solution(5))
print(solution2(3))
print(solution2(5))

# n	return
# 3	"수박수"
# 4	"수박수박"