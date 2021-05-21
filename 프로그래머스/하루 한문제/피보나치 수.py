def solution(n):
    fb = [0 for _ in range(n+1)]
    fb[0] = 0; fb[1] = 1

    for i in range(2,n+1):
        fb[i] = fb[i-2] + fb[i-1]
    return fb[n] % 1234567

print(solution(3))

# n	return
# 3	2
# 5	5