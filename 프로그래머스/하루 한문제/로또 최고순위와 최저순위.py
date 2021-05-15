from collections import Counter
def solution(lottos, win_nums):
    answer = []
    dic1 = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    c1 = Counter(lottos)
    c2 = Counter(win_nums)
    c3 = c1&c2

    answer.append(dic1[len(c3)]) # 최저순위
    answer.append(dic1[len(c3) + c1[0]]) if c1[0] <= len(c2 - c3) else answer.append(dic1[len(c3) + len(c2 - c3)]) # 최고순위

    return sorted(answer)

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
# lottos	win_nums	result
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]