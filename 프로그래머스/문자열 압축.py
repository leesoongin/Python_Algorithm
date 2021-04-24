def solution(s):
    answer = 0
    lengthList = list()

    if len(s) == 1:
        return 1

    for size in range(1, len(s) // 2 + 1):
        result = ''
        standard = s[:size]
        count = 1
        for i in range(size, len(s), size):  # 크기만큼 잘라버리기 3 6 9 ...
            if s[i:i + size] == standard:
                count += 1
            else:  # 끊기면
                if count == 1:
                    count = ''
                result += str(count) + standard
                standard = s[i:i + size]
                count = 1
        if count == 1:
            count = ''
        result += str(count) + standard
        lengthList.append(len(result))

    answer = min(lengthList)
    return answer