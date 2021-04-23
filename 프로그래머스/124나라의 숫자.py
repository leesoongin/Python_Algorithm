# def solution(n):
#     answer = ''
#
#     arr = ['4','1','2']
#
#     while n>0:
#         n, mod = divmod(n, 3)
#         print(n,mod)
#         if n < 3:
#             answer = arr[n] + answer
#
#         else:
#             answer = arr[mod] + answer
#
#
#     print(answer)
#     return answer

def solution(num):
    answer = ""

    while num:
        num, nam = divmod(num, 3)
        print(num,nam)
        answer = "412"[nam] + answer
        if nam == 0:
            num -= 1

    print(answer)
    return answer

solution(1000)