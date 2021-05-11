from itertools import combinations

def solution(nums):
    numSet = set(nums)

    if len(numSet) < len(nums)//2:
        return len(numSet)
    else:
        return len(nums)//2


print(solution([3,3,3,2,2,4]))
# 중복제거해버리면 일단 편함
# 수 절반보다 종류가다양하지 않으면 종류수만큼 return
# 수 절반보다 종류가 다양하다면 == 내가 뽑은 녀석들은 다 다른녀석들이니까, 뽑은수만큼 return

# [3,1,2,3]	2
# [3,3,3,2,2,4]	3
# [3,3,3,2,2,2]	2