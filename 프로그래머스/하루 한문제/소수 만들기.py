from itertools import combinations
def solution(nums):
    answer = 0
    comList = list(combinations(nums,3))

    for item in comList:
        if isPrime(item):
            answer += 1

    return answer

def isPrime(item):
    for i in range(2,sum(item)):
        if sum(item) % i == 0:
            return False
    return True
print(solution([1,2,7,6,4]))

# 세 수를 뽑아 소수가 되는 경우의 수를 return
# 세 수를 뽑아서 더한 후, 소수가 되는지 판단
# 소수라면 임시 리스트에 저장
# 리스트의 len을 return
# 소수의 조건 : 1과 자기자신으로만 나누어 떨어져야 한다.