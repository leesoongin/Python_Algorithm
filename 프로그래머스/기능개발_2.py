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