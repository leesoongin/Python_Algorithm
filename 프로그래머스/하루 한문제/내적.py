def solution(a, b):
    return sum(a[index]*b[index] for index in range(len(a)))