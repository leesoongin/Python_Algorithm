# scores	result
# [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]	"FBABD"
# [[50,90],[50,87]]	"DA"
# [[70,49,90],[68,50,38],[73,31,100]]	"CFD"
# 첫째, 0,1,2,3,4의 평가점수로 배열만들고 [o]
    # 그 안에서 유일한 최고 최저점을 찾고
    # 평균을 구해서 학생 학점을 평가 하면 됨
def solution(scores):
    answer = ''
    userScore = [[0 for _ in range(len(scores))] for _ in range(len(scores))]

    for i in range(len(scores)):
        for j in range(len(scores)):
            userScore[i][j] = scores[j][i]

    for index,items in enumerate(userScore):
        if items[index] == max(items) and items.count(max(items)) == 1 : # 내 평가가 최댓값이고, 유일한 최고점일 경우
            items.remove(items[index])
        elif items[index] == min(items) and items.count(min(items)) == 1 : # 내 평가가 최솟값이고, 유일한 최저점일 경우
            items.remove(items[index])

    for items in userScore:
        avg = sum(items)/len(items)

        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])
solution([[50,90],[50,87]])
solution([[70,49,90],[68,50,38],[73,31,100]])
