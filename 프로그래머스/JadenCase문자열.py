
def solution(s):
    answer = ''
    s1 = s.split(' ')
    for item in s1:
        if item == '':
            answer += " "
        elif item[0].isalpha():
            answer += item[0].upper()+item[1:].lower() + " "
        else:
            answer += item.lower() + " "

    return answer[:-1]

# print(solution("3people unFollowed me"))
# print(solution("3"))
# print(solution("e"))
print(solution("        3people unFollowed me"))
print(solution("        "))
# s	return
# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	"For The Last Week"