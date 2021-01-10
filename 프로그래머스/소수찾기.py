from itertools import permutations

def solution(numbers):
    answer = 0
    result=[]
    resultSet=set()

    for i in range(len(numbers)):
        result.append(set(map(''.join,permutations(numbers,i+1))))

    for i in result:
        for j in i:
            resultSet.add(int(j))

    print(resultSet)
    for i in resultSet:
        if prime(i):
            answer+=1

    return answer

def prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return True

numbers="011"
print(solution(numbers))
