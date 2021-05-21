from itertools import combinations
from collections import defaultdict

def solution(infos,queries):
    answer = []
    info_dict = defaultdict(list)
    # 각각의 info로 만들 수 있는 모든 경우의 수를 만들어 놓는다
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_value = int(info[-1])
        for i in range(5):
            for combi in combinations(info_key,i):
                tmp_key = ''.join(combi)
                info_dict[tmp_key].append(info_value)
    # value값으로 가지고 있는 점수들을 오름차순으로 정렬하자 -> 이따 해당 점수 이상을 만족하는걸 찾기위해 ->(lower bounder)방식을 사용하기 위해 asd
    for key in info_dict.keys():
        info_dict[key].sort()

    # 각각의 query 를 꺼내 아까 만든 딕셔너리에 해당하는 경우가 존재한다면 그 값을 꺼내고(해당하는 조건을 만족하는 경우들의 점수들) 해당조건 이상의 값들이 몇개있는지 찾는다
    for query in queries:
        query = query.replace("and",'').replace('  ','').replace('-','').split()
        query_score = int(query[-1])
        query = query[:-1]
        tmp_query = ''.join(query)
        if tmp_query in info_dict: # 해당하는 조건을 만족하는 지원자가 존재한다면
            scores = info_dict[tmp_query]
            if len(scores) > 0: # lower bounder 를 이용해 어느 값 이상의 값을 가지는 인덱스값을 찾는다. 그 인덱스 값부터는 다 조건을만족하는 수 들임
                start,end = 0,len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores)-start) # answer.append(len(scores)-end 해도 같을걸?
        else: # 해당하는 경우가 존재하지 않는다면
            answer.append(0)
    return answer

print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]
               ))


# info	query	result
# ["java backend junior pizza 150","python frontend senior chicken 210",
#  "python frontend senior chicken 150","cpp backend senior pizza 260",
#  "java backend junior chicken 80","python backend senior chicken 50"]
# ["java and backend and junior and pizza 100",
#  "python and frontend and senior and chicken 200",
#  "cpp and - and senior and pizza 250",
#  "- and backend and senior and - 150",
#  "- and - and - and chicken 100",
#  "- and - and - and - 150"]
# [1,1,1,1,2,4]