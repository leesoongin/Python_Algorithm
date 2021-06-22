def solution2(s):
    stack = list()
    for ele in s:
        if len(stack) == 0:
            stack.append(ele)
        elif stack[-1] == ele:
            stack.pop()
        else:
            stack.append(ele)
    return 1 if len(stack) == 0 else 0

print(solution2("baabaa"))


from collections import deque

def solution(s):
    stack = deque()

    for item in s:
        if len(stack) == 0:
            stack.append(item)
        elif stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)

    # 다 된경우
    if len(stack) == 0:
        return 1
    return 0


print(solution("baabaa"))