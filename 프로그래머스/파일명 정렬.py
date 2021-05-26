# def solution(files):
#     answer = []
#     head = []
#     number = []
#     tail = []
#     tmp = []
#     s = [file for file in files]
#     s_list = []
#     #나눠보자
#     for file in files:
#         for i in range(len(file)):
#             if file[i].isdigit():
#                 head.append(file[:i])
#                 tmp.append(file[i:])
#                 break
#     for item in tmp:
#         t2 = ''
#         for i in range(len(item)):
#             if item[i].isdigit() and len(item[:i+1]) <= 5:
#                 t2 += item[i]
#             else:
#                 tail.append(item[i:])
#                 break
#         number.append(t2)
#
#     # 나눴고 이제 정렬하면 된다
#
#     for i in range(len(files)):
#         s_list.append([head[i].lower(),int(number[i]),s[i]])
#     tmp2 = sorted(s_list,key=lambda x : (x[0],x[1]))
#
#     for item in tmp2:
#         answer.append(item[2])
#
#     return answer
#
#
#
# print(solution(["img122222222222.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# # print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# # 정렬시 head는 사전순으로 정렬 영어 대소문자 구분은 안함
# # head에서 정렬차이가 없을경우 두번째 우선순위로 number의 숫자순으로 정렬한다
# # 만약 앞의 두 경우에서 정렬이 안될경우 그대로 나오면 된다.
#
# # 파일명	HEAD	NUMBER	TAIL
# # foo9.txt	foo	9	.txt
# # foo010bar020.zip	foo	010	bar020.zip
# # F-15
#
# # HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
# # NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
# # TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.
#
# # 입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# # 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# #
# # 입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# # 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
#
import re
def solution(files):
    d = dict()
    for i in files :
        init = []
        answer = re.findall('\D+|\d+',i)
        init.append(answer[0].lower())
        init.append(int(answer[1]))
        d[i] = init
    d = sorted(d.items(), key=lambda x:(x[1][0],x[1][1]))
    answer = []
    for i in d :
        answer.append(i[0])

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))