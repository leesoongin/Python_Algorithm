def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i].islower() and ord(s[i])+n > ord('z'):
            answer += chr(ord(s[i])+n - 26)
        elif s[i].isupper() and ord(s[i])+n > ord('Z'):
            answer += chr(ord(s[i])+n - 26)
        elif s[i] == ' ':
            answer += ' '
        else:
            answer += chr(ord(s[i])+n)

    return answer

def solution2(s,n):
    s = list(s)

    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n)%26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n)%26 + ord('a'))

    return ''.join(s)

# 아스키코드  문자 -> 아스키코드 : ord()  //  아스키코드 -> 문자  : chr()
# 마지막 문자인 z에서의 예외만 처리하면 쉬운 문제   z: 122
print(solution("xYz",3))
print(solution2("xYz",3))
# s	n	result
# "AB"	1	"BC"
# "z"	1	"a"
# "a B z"	4	"e F d"