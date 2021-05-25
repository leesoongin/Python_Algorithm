
def solution(people, limit):
    answer = len(people)
    p = sorted(people,reverse = True)
    s,e = 0, len(p)-1

    # 무거운놈부터 보내
    while s < e :
        if p[s]+p[e] <= limit : # 짝지어서 나갈수으면 보내고 보트수 줄이기
            e-=1
            answer-=1
        s+=1
    return answer

print(solution([70, 50, 80, 50],100))
print(solution([20, 50, 50, 80,40,50,45,45,100],100))
# people	limit	return
# [70, 50, 80, 50]	100	3
# [70, 80, 50]	100	3