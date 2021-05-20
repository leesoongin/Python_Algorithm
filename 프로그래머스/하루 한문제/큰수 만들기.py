def solution(number,k):
    stack = [number[0]]

    for i in range(1,len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
    while k > 0 :
        stack.pop()
        k -= 1
    return ''.join(stack)

def solution2(number,k):
    stack = [number[0]]

    for i in range(1,len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
    return ''.join(stack[:len(stack)-k])



print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("11441",4))


# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"
# 11111131333
