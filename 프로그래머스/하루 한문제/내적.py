def solution2(a,b):
    return sum(a[i] * b[i] for i in range(len(a)))



# a	b	result
# [1,2,3,4]	[-3,-1,0,2]	3
# [-1,0,1]	[1,0,-1]	-2





def solution(a, b):
    return sum(a[index]*b[index] for index in range(len(a)))