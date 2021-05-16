def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        s1 = bin(arr1[i] | arr2[i])[2:].replace('1','#').replace('0',' ')
        while len(s1) < n:
            s1 = ' ' + s1
        answer.append(s1)

    return answer

def solution2(n,arr1,arr2):
    return [ bin(arr1[i] | arr2[i])[2:].replace('1','#').replace('0',' ').rjust(n,' ') for i in range(len(arr1)) ]

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

print(solution2(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution2(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))

# n	5
# arr1	[9, 20, 28, 18, 11]
# arr2	[30, 1, 21, 17, 28]
# 출력	["#####","# # #", "### #", "# ##", "#####"]


# n	6
# arr1	[46, 33, 33 ,22, 31, 50]
# arr2	[27 ,56, 19, 14, 14, 10]
# 출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
