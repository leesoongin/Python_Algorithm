def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        if not signs[i]:
            answer -= absolutes[i]
        else:
            answer += absolutes[i]
    return answer

# def solution(absolutes, signs):
#     answer = 0

#     for index,sign in enumerate(signs):
#         if not sign:
#             answer -= absolutes[index]
#         else:
#             answer += absolutes[index]
#     return answer