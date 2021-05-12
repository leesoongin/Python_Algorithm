from collections import Counter
from itertools import permutations
import re
def solution(expression):
    answer = 0
    prioOper = list(permutations('+-*',3))
    operatorList = Counter(''.join(re.findall("\D", expression)))
    answerlist = []

    for oper in prioOper:
        equation = re.findall('\d+|\D', expression)
        for op in oper:
            for _ in range(operatorList[op]):
                targetIndex = equation.index(op)
                eq = equation[targetIndex-1]+equation[targetIndex]+equation[targetIndex+1]
                del equation[targetIndex-1]; del equation[targetIndex-1]; del equation[targetIndex-1];
                equation.insert(targetIndex-1,str(eval(eq)))
        answerlist.append(abs(eval(equation[0])))
    return max(answerlist)
print(solution("100-200*300-500+20"))
# "100-200*300-500+20"	60420
# "50*6-3*2"

# a = dict()
# a['x'] = []
# a["x"].append(1)
# print(a)