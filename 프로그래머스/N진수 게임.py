def solution(n, t, m, p):
    answer = ''
    s1 = ''
    for num in range(t*m):
        if len(s1) < t*m:
            s1 += convert(num,n)

    for i in range(len(s1)):
        if i % m == p-1 and i < t * m:
            answer += s1[i]

    return answer

def convert(num, base):
    rev_base = ''
    if num == 0:
        return '0'
    while num > 0:
        num, mod = divmod(num, base)
        if mod == 10:
            rev_base += 'A'
        elif mod == 11:
            rev_base += 'B'
        elif mod == 12:
            rev_base += 'C'
        elif mod == 13:
            rev_base += 'D'
        elif mod == 14:
            rev_base += 'E'
        elif mod == 15:
            rev_base += 'F'
        else:
            rev_base += str(mod)
    print(rev_base)
    return rev_base[::-1]


# print(solution(2,4,2,1))
print(solution(16,16,2,2))
# 입출력 예제
# n	t	m	p	result
# 2	4	2	1	"0111"
# 16	16	2	1	"02468ACE11111111"
# 16	16	2	2	"13579BDF01234567"

# 진법 n,
# 미리 구할 숫자의 갯수 t,
# 게임에 참가하는 인원 m,
# 튜브의 순서 p 가 주어진다.