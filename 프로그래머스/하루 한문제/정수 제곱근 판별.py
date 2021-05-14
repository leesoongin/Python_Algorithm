import math

def solution(n):
    num = n ** (1 / 2)
    if num % 1 == 0:
        return int((num+1) ** 2)
    else:
        return -1

def solution2(n):
    if math.sqrt(n) % 1 == 0:
        return pow(math.sqrt(n)+1,2)
    return -1

print(solution(121))
print(solution(3))
print(solution2(121))
print(solution2(3))
# 제곱근 판별 어케함