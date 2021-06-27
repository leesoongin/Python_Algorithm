def solution(s):
    l = s.split(" ")
    answer = ""

    for item in l:
        for i in range(len(item)):
            if i % 2 == 0: # 짝수라면
                answer += item[i].upper()
            else:
                answer += item[i].lower()
        answer += " "
    return answer[:-1]

print(solution("try hello world"))

# 입출력 예
# s	return
# "try hello world"	"TrY HeLlO WoRlD"
