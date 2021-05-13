# 첫번째 풀이,
def solution(n):
    answer = 0
    sam = list()

    while n > 0:
        n,mod = divmod(n,3)
        sam.append(mod)
    for i in range(len(sam)):
        answer += sam[i] * 3**(len(sam)-(1+i))

    return answer

# n진법 -> 10진법으로 바꾸는데에 int('0021',n진법) 으로 가능
def solution2(n):
    sam = list()

    while n > 0:
        n,mod = divmod(n,3)
        sam.append(str(mod))
    answer = int(''.join(sam),3)
    return answer

print(solution(45))
print(solution2(45))


# n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
# 45	1200	0021	7