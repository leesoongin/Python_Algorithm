from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for i in course:
        t1 = []
        for order in orders:
            t1.extend(list(combinations(sorted(order),i)))
        for key,value in Counter(t1).items():
            if value == max(Counter(t1).values()) and value > 1:
                answer.append(''.join(key))
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))

# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
# ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
# ["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]