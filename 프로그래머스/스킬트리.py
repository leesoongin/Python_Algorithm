#

import re

def solution(skill,skill_trees):
    answer = 0
    alphas = list()
    answerList = list()
    trueCase = list()

    for i in range(len(skill)+1):
        str1 = ""
        for j in range(1, i + 1):
            str1 += str(j)
        trueCase.append(str1)

    for i in skill:
        alphas.append(i)

    for i in range(len(skill_trees)):
        for index,j in enumerate(range(len(alphas))):
            skill_trees[i] = skill_trees[i].replace(alphas[j],str(index+1))

    for item in skill_trees: # 문자열로만들
        str1 = ''
        for numStr in re.findall("\d+", item):
            str1 += numStr
        answerList.append(str1)

    print(trueCase)
    for i in range(len(answerList)):
        for case in trueCase:
            if answerList[i] == case:
                answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA","CDBDB"]

solution(skill,skill_trees)
