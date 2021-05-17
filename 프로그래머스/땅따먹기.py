def solution(land):
    dp = [[0,0,0,0] for _ in range(len(land))]

    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(len(land)):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])

    return max(dp[len(land)-1])

# def test(index,land):


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
print(solution([[4, 3, 2, 1],
                [2, 2, 2, 1],
                [6, 6, 6, 4],
                [8, 7, 6, 5]]))
# [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
# [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	16

# if index == 0:
        #     answer = max(item)
        #     print(answer)
        #     postIndex = item.index(max(item))
        # else:
        #     item[postIndex] = 0
        #     answer += max(item)
        #     print(answer)
        #     postIndex = item.index(max(item))