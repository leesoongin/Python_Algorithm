def solution(progresses, speeds):
    answer = list()

    while(progresses):
        count = 0
        for index,(_,speed) in enumerate(zip(progresses,speeds)):
            progresses[index] += speed
        for item in progresses:
            if item < 100:
                break
            count += 1

        for _ in range(count):
            progresses.pop(0)
            speeds.pop(0)

        if count > 0:
            answer.append(count)

    return answer


solution([93, 30, 55],[1, 30, 5])

# 다른사람풀이 time이라는 변수를 이용해 시간이 변화할때마다의 값을 이용할수있게했네 개똑똑한듯;

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer