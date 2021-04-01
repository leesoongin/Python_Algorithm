
from itertools import permutations

def solution(numbers):
    answer = 0
    permuArr = []
    answerArr = set()

    for i in range(1,len(numbers)+1):
        permuArr.append(set(map(''.join,permutations(numbers,i))))

    for items in permuArr:
        for item in items:
            if isPrime(item):
                answerArr.add(int(item))

    answer = len(answerArr)
    return answer

def isPrime(number):
    if int(number) <= 1:
        return False

    for i in range(2,int(number)):
        if int(number) % i == 0:
            return False
    #안 걸렸으
    return True
