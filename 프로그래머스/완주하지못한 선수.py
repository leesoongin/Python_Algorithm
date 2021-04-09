# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

#효율성 0점 ,, for문 한번에 remove에서 o(n)겹쳐서  시간복잡도 - > o(n2) ..
def solution(participant,completion):
    answer = ''
    for comple in completion:
        participant.remove(comple)
    answer = participant[0]

    return answer

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])

# 배열간의 - 가 가능하네 Counter 라는녀석이 좀 만능이
# import collections
# def solution(participant,completion):
#     answer = ''
#
#     answer = collections.Counter(participant) - collections.Counter(completion)
#
#     return list(answer.keys())[0]

# # 효율성..이렇게도 푸는데 음 별로 !
# def solution(participant, completion):
#     answer = ''
#     participant = sorted(participant)
#     completion = sorted(completion)
#
#     for index in range(len(completion)):
#         if participant[index] != completion[index]:
#             return participant[index]
#
#     return participant[-1]
#
#
# # 효율성 o(n)이 되야 통과인듯

