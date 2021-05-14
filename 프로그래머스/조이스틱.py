# 정방향 , 최댓값 - 정방향 + 1

# #abcdefghijklmnopqrstuvwxyz
def solution(name):
    name = list(name)
    answer = 0
    i = 0

    while True:
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        name[i] = 'A'

        if name.count('A') == len(name):
            print(answer)
            return answer

        left, right = 1, 1
        for l in range(1, len(name)):
            if name[i - l] == 'A':
                left += 1
            else:
                break

        for r in range(1, len(name)):
            if name[i + r] == 'A':
                right += 1
            else:
                break

        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right

    return answer
solution('JAN')


# def solution(name):
#     answer = 0
#     alphaSize = 26
#     standardCharacter = 'A'
#     forwordResult = 0
#     reverseResult = 0
#     if name.count('A') == len(name): # 전부다 A라면
#         print(0)
#         return 0
#     if name[1] == 'A': # 특수케이스
#         for index,item in enumerate(name):
#             if index == 1 and item == 'A': # 두번째 원소일때
#                 continue
#             forword = ord(item) - ord(standardCharacter)
#             reverse = alphaSize - (forword + 1) + 1
#             print("2 ",forword,reverse)
#             if forword > reverse:
#                 reverseResult += reverse
#             else:
#                 reverseResult += forword
#         reverseResult += 1
#         print(reverseResult)
#         return reverseResult
#     else: # 정
#         for index, item in enumerate(name):
#             forword = ord(item) - ord(standardCharacter)
#             reverse = alphaSize - (forword + 1) + 1
#             print("1 ", forword, reverse)
#             if forword > reverse:
#                 forwordResult += reverse
#             else:
#                 forwordResult += forword
#         forwordResult += len(name) - 1
#         print(forwordResult)
#         return forwordResult
#
#
# solution("BBBAAAB")