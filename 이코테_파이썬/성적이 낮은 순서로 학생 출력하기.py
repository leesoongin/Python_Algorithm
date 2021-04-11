def solution(arr):
    answer = list()

    answer = sorted(arr,key=lambda x : x[1])

    print(answer)
    return answer

solution([["홍길동",95],["이순신",77],["이순신",1],["이순신",2],["이순신",3]])