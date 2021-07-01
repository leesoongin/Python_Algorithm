import string
def solution(msg):
    answer = []
    d1 = dict()
    tmp = ''
    # 사전 생
    for i in range(len(string.ascii_uppercase)):
        d1[string.ascii_uppercase[i]] = i + 1

#일치하는 가장 긴 문자열을 어케 찾냐???? ->
    for ele in msg:
        tmp += ele
        if d1.get(tmp) == None:
            answer.append(d1[tmp[:-1]])
            d1[tmp] = len(d1) + 1
            tmp = tmp[-1:] # 입력된거 제거하고 나머지만 넣자
    answer.append(d1[tmp])

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))


# msg	answer
# KAKAO	[11, 1, 27, 15]
# TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# ABABABABABABABAB	[1, 2, 27, 29, 28, 31, 30]