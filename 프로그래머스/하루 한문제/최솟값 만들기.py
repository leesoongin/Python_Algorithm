
def solution(A, B):
    A = sorted(A)
    B = sorted(B,reverse=True)
    return sum([A[i]*B[i] for i in range(len(A))])

print(solution([1, 4, 2],[5, 4, 4]))
# A	B	answer
# [1, 4, 2]	[5, 4, 4]	29
# [1,2]	[3,4]	10
