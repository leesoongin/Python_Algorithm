
# 식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 가장 많이 맞춘사람

from itertools import cycle

def solution(answers):
    answer = []

    one_arr = [1,2,3,4,5]
    two_arr = [2,1,2,3,2,4,2,5]
    three_arr = [3,3,1,1,2,2,4,4,5,5]
    answer_count_arr = [0,0,0]

    for (one,two,three,item) in zip(cycle(one_arr),cycle(two_arr),cycle(three_arr),answers):
        if one == item:
            answer_count_arr[0] += 1
        if two == item:
            answer_count_arr[1] += 1
        if three == item:
            answer_count_arr[2] += 1

    for (index,item) in enumerate(answer_count_arr):
        if item == max(answer_count_arr):
            answer.append(index+1)

    return answer

solution([1,2,3,4,5])
