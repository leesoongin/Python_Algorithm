from collections import defaultdict


def solution(genres, plays):
    answer = []
    d1 = defaultdict(list)
    prioDict = list()

    # 재생시간, 우선순위벼로 묶음
    for i in range(len(genres)):
        d1[genres[i]].append([plays[i], i])

    for key in d1.keys():
        tmp = 0
        for item in d1[key]:
            tmp += item[0]
        prioDict.append([tmp, key])
    prioDict = sorted(prioDict, key=lambda x: -x[0])

    for play, genre in prioDict:
        d1[genre] = sorted(d1[genre], key=lambda x: (-x[0], x[1]))
        # print(d1[genre])
        if len(d1[genre]) == 1:
            answer.append(d1[genre][0][1])
        else:
            for i in range(0, 2):
                answer.append(d1[genre][i][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]