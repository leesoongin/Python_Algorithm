def solution(n,a,b):
    answer = 0

    while True:
        if a==b:
            break
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2

    return answer
    # 각각의 칸으로 나뉨
    # 12 34 56 78
    # 1번이든 2번이든 무조건 1
    # 3번이든 4번이든 무조건 2
    # 5번 6번도 무조건 3
    # 7번 8번도 무조건 4

    # 계속가면 1 2
    # 이런식으로 계속 2배씩 줄어들음

    # 따라서
    # 각 원소의 수 +1 /2 를 하면 결국 그 숫자가 이겼을 경우에 몇번이 되는지 구할 수 있




print(solution(8,4,7))
