def solution(bridge_length,weight,truck_weights):
    answer=0
    passingQueue=[0 for _ in range(bridge_length)]

    while passingQueue:
        answer+=1
        passingQueue.pop(0)

        if truck_weights:
            if sum(passingQueue) + truck_weights[0] <= weight:
                passingQueue.append(truck_weights.pop(0))
            else:
                passingQueue.append(0)

    return answer



truck_weights = [7,4,5,6]
bridge_length = 2
weight = 10

print(solution(bridge_length,weight,truck_weights))
