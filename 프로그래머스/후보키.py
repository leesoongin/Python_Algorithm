from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 모든 튜플이 이루어질 수 있는 경우의 수를 조합해서 만들어놓기
    candidate = []
    for i in range(1,col + 1):
        candidate.extend(combinations(range(col),i))

    # 유일성 조건. 각각의 속성값으로 튜플을 만들었을때, 중복되는 튜플이 있다면 유일성을 만족하지 못함.
    # 튜플이 elation의 row개 만큼 나와야함 더 적다면 중복되는게 속성의 값들 중 중복되는 값이 존재한다는 의미
    unique = []
    for candi in candidate:
        tmp = [tuple(item[i] for i in candi) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candi)
    # 최소성 조건 이미 후보키를 만족하는 키를 포함하는 키가 존재할 경우, 최소한의 속성을 가진 튜플을 포함하는 튜플을 제거
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if set(unique[i]) == (set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    # 유일성, 최소성을 만족하는 튜플이 answer에 저장.
    return len(answer)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# relation	result
# [["100","ryan","music","2"],
# ["200","apeach","math","2"],
# ["300","tube","computer","3"],
# ["400","con","computer","4"],
# ["500","muzi","music","3"],
# ["600","apeach","music","2"]]	2