# 1로 만들기의 경우 3가지가 존재함
#
# case 1 : -1   // case 2: 2로 나누기   // case 3: 3으로 나누기
#
#


def solution(n):
    dp = [0 for _ in range(n+1)]# 연산의 최소 횟수를 저장할 dp배열
    # 1로 만들기
    #
    for i in range(2,n+1):
        dp[i] = dp[i-1] + 1 # 1을 뺀 경우
        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i//2] + 1) # 1을 뺸 값이랑, 2를 나눠서 나온 값이랑 비교해서 더 작은값을 저장
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1) # 1을 뺀 값이랑, 3을 나눠서 나온 값이랑 비교해서 더 작은값을 저장
    return dp[n]
print(solution(10)) # 3
print(solution(2)) # 1