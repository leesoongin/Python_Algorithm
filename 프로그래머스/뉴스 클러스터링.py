import re
from collections import Counter

def solution(str1,str2):
    # 문자열에서 필요한 놈들만 추출하
    str1List = re.findall('[a-zA-Z]+',str1); str2List = re.findall('[a-zA-Z]+', str2)
    # 이놈들이 부분집합을 가지고 있는 집합이라고 생각하자
    test1List = list() ;test2List = list()

    for item in str1List:
        for i in range(len(item)-1):
            test1List.append(item[i].lower()+item[i+1].lower())
    for item in str2List:
        for i in range(len(item)-1):
            test2List.append(item[i].lower()+item[i+1].lower())
    oneCounter = Counter(test1List); twoCounter = Counter(test2List)

    imGgoSet = set(test1List) & set(test2List)
    ggoset = len(imGgoSet)
    for item in imGgoSet:
        if oneCounter[item] > twoCounter[item]:
            ggoset += twoCounter[item] - 1 # 중복제거로 제거되지 않은 하나의 개수를 - 해주고 count한 값들을 더해주는 느낌으로
        else:
            ggoset += oneCounter[item] - 1 # 중복제거로 제거되지 않은 하나의 개수를 - 해주고 count한 값들을 더해주는 느낌으로
    imHapset = set(test1List) | set(test2List)
    hapset = len(imHapset)

    for item in imHapset:
        if oneCounter[item] > twoCounter[item]:
            hapset += oneCounter[item] - 1
        else:
            hapset += twoCounter[item] - 1

    if ggoset == 0 and hapset == 0 :
        return 1 * 65536
    elif ggoset == 0:
        return 0
    else:
        return int((ggoset / hapset) * 65536)

print(solution("E=M*C^2","e=m*c^2"))


