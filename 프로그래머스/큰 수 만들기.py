from itertools import combinations

def solution(number, k):
    answer = ''

    resultList = list(map(''.join,combinations(number,len(number)-k)))
    # 리스트 컴프리텐션
    return max(resultList)

solution("4177252841",4)