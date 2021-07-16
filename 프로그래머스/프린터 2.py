def solution(priorities, location):
    cnt = 0
    queue = list()

    for index, item in enumerate(priorities):
        queue.append([index, item])

    while queue:
        curr = queue.pop(0)
        if any(curr[1] < item[1] for item in queue):
            queue.append(curr)
        else:
            cnt += 1
            if curr[0] == location:
                return cnt
    return cnt