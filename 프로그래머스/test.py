import re
def solution(s):
    answer = 0
    alphaToNum = {'zero':0,'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for key in alphaToNum.keys():
        if key in s :
            s = s.replace(key,str(alphaToNum[key]))
    print(s)
    answer = int(s)
    return answer

solution("one4seveneight")


def test1():
    print(re.findall('[a-zA-Z]+',"aa1+aa2"))
    return

print(test1())