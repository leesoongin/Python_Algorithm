import numpy as np

def solution(arr1, arr2):
    answer = list()
    for a,b in zip(arr1,arr2):
        t1 = list()
        for c,d in zip(a,b):
            t1.append(c+d)
        answer.extend([t1])
    return answer

def solution2(arr1,arr2):
    return [[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]

def solution3(arr1,arr2):
    return (np.array(arr1) + np.array(arr2)).tolist()

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution2([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution3([[1,2],[2,3]],[[3,4],[5,6]]))
# arr1	arr2	return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]