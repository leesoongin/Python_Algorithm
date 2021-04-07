
# range(len(arr)) -> 로 돌리면 범위는 0 ~ len(arr)-1  까지임.  그니까 따로 range에서 -1하지말자,,
def solution(board, moves):
    answer = 0
    bowl = list()

    for move in moves:
        for index in range(len(board)):
            if board[index][move-1] != 0: # 빈 공간이 아니라면 바구니에 넣자
                bowl.append(board[index][move-1])
                board[index][move-1] = 0
                break
        if len(bowl) > 1:
            if bowl[-1] == bowl[len(bowl)-2]: # 마지막과, 그 앞의 원소가 같다면
                bowl.pop()
                bowl.pop()
                answer += 2

    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])
