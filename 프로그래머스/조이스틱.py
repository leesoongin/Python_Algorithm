# 정방향 , 최댓값 - 정방향 + 1

#abcdefghijklmnopqrstuvwxyz
def solution(name):
    answer = 0
    alphaSize = 26
    standardCharacter = 'A'
    forwordResult = 0
    reverseResult = 0
    if name.count('A') == len(name): # 전부다 A라면
        print(0)
        return 0
    if name[1] == 'A': # 특수케이스
        for index,item in enumerate(name):
            if index == 1 and item == 'A': # 두번째 원소일때
                continue
            forword = ord(item) - ord(standardCharacter)
            reverse = alphaSize - (forword + 1) + 1
            print("2 ",forword,reverse)
            if forword > reverse:
                reverseResult += reverse
            else:
                reverseResult += forword
        reverseResult += 1
        print(reverseResult)
        return reverseResult
    else: # 정
        for index, item in enumerate(name):
            forword = ord(item) - ord(standardCharacter)
            reverse = alphaSize - (forword + 1) + 1
            print("1 ", forword, reverse)
            if forword > reverse:
                forwordResult += reverse
            else:
                forwordResult += forword
        forwordResult += len(name) - 1
        print(forwordResult)
        return forwordResult


solution("BBBAAAB")