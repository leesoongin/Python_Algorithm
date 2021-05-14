def solution(s):
    return s.isdigit() and len(s) ==4 or len(s) == 6

def solution2(s):
    return s.isdigit() and len(s) in (4,6)

print(solution("1234"))
print(solution("a234"))
print(solution2("1234"))
print(solution2("a234"))
# s	return
# "a234"	false
# "1234"	true