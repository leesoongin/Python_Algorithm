def solution(numbers):
    answer=''
    numbers=list(map(str,numbers))
    answer=''.join(sorted(numbers,key=lambda x:(x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse=True))

    if int(answer) == 0:
        answer = '0'
        return answer

    return answer

# len 1 -> 0 0 0 0 -> 0
# len 2 -> 0 1 0 1 -> 0 1
# len 3 -> 0 1 2 0 -> 0 1 2
# len 4 -> 0 1 2 3 -> 0 1 2 3


numbers =[0,0]
print(solution(numbers))