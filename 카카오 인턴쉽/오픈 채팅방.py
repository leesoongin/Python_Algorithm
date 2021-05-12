def solution(record):
    answer = []
    manager = list()
    users = dict()
    # 나누고
    for item in record:
        manager.append(item.split(' ')[0]+' '+item.split(' ')[1])
        if item.split(' ')[0] != "Leave":
            users[item.split(' ')[1]] = item.split(' ')[2]
    for item in manager:
        temp = item.split(' ')
        if temp[0] == "Enter":
            answer.append(users[temp[1]]+"님이 들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(users[temp[1]]+"님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# 입 출력
# ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]