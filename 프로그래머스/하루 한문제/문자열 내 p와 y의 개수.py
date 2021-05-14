from collections import Counter
def solution(s):
    s= s.lower()
    alphaCount = Counter(s)

    if alphaCount['p'] == alphaCount['y'] or alphaCount['p'] and alphaCount['y'] == 0 :
        return True
    return False

def solution2(s):
    p = s.lower().count('p')
    y = s.lower().count('y')

    if p == y :
        return True
    return False

def solution3(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    return False

print(solution("pPoooyY"))
print(solution("Pyy"))
# s	answer
# "pPoooyY"	true
# "Pyy"	false