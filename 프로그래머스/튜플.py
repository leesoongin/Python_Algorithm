#하나짜리가 맨 앞자리
# 두개짜리에서 맨앞자리를 제외한 나머지가 2번쨰 자리
# 세개짜리에서 앞의 두개를 제외한 나머지가 3번째 자리
# 네개짜리에서 앞의 세개를 제외한 나머지가 4번째자리

def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)


    while s:
        numSet = s.pop(0)
        numSet = numSet.split(',')

        for char in numSet:
            if char.isdigit() and char not in answer:
                answer.append(char)

    return list(map(int,answer))


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{20,111},{111}}"))

