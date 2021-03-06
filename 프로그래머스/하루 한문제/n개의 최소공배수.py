from functools import reduce

def solution2(arr):
    # return reduce(lcm,arr)
    return reduce(lambda a,b: a*b//gcd(a,b),arr)
def solution(arr):
    answer = lcm(arr[0],arr[1])

    for i in range(2,len(arr)):
        answer = lcm(answer,arr[i])

    return answer

def gcd(x,y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)


print(solution2([2,6,8,14]))
print(solution([2,6,8,14]))
# arr	result
# [2,6,8,14]	168
# [1,2,3]	6

print(gcd(78696,19332))