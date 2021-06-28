from collections import defaultdict
from functools import reduce

def solution(clothes):
    d1 = defaultdict(list)
    for name, kind in clothes:
        d1[kind].append(name)
    l = [len(value) for key, value in d1.items()]
    l[0] += 1
    answer = reduce(lambda x,y : x*(y+1),l) - 1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

# clothes	return
# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3