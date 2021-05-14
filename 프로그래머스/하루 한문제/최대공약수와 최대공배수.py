def solution(n, m):
    return [gcd(n,m),lcm(n,m)]

def gcd(x,y):
    while y:
        x,y = y , x % y
    return x

def lcm(x,y):
    return x*y // gcd(x,y)

print(solution(2,5))
print(solution(3,12))

# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]