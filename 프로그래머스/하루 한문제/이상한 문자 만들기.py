def solution(s):
    answer = ''
    wordList = s.split(' ')

    for item in wordList:
        temp = list(item)
        for i in range(len(temp)):
            if i % 2 == 0:
                temp[i] = temp[i].upper()
            else:
                temp[i] = temp[i].lower()
        answer += ''.join(temp)+' '

    return answer[:-1]

print(solution("try hello world"))
# 풀이
# 1. 공백의 개수를 구한다
# 2. splite으로 나눠 단어별로 짝수번째 인덱스는 대문자로, 홀수번쨰 인덱스는 소문자로 변환한다    // 이떄, lower , upper 사용
# 3. 변환한 단어들을 사이에 공백을 넣어 return 한다.


# s	return
# "try hello world"	"TrY HeLlO WoRlD"