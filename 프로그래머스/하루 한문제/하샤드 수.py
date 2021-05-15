from  functools import reduce
def solution(x):
    # return True if x % sum([int(item) for item in str(x)]) == 0 else False
    return x % sum([int(item) for item in str(x)]) == 0

print(solution(10))


# arr	return
# 10	true
# 12	true
# 11	false
# 13	false