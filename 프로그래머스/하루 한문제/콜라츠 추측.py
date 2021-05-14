def solution(num):
    return test(num,0)

def test(num,count):
    if num == 1 :
        return count
    elif count >=500:
        return -1
    else:
        if num % 2 == 0:
            count += 1
            return test(num//2,count)
        else:
            count +=1
            return test((num * 3) + 1,count)

print(solution(626331))


# n	result
# 6	8
# 16	4
# 626331