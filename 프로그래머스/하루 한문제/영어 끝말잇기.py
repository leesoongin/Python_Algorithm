# 사이클 돌때마다 하나 ++
    # 차례를 %n연산으로 0이면 1번사람, 1이면 2번사람, 2면 3번사람 탈락
    # 몇번사람, 몇번차례에 탈락하는지 return
    # 탈락의 조건은 -> 이전에 등장했던 단어 or 앞글자를 맞추지 못했을 경우

def solution(n, words):
    count = 1
    # 3 -> 312 / 4 -> 4123 5 -> 51234
    peopleNum = [item for item in range(1,n)]
    peopleNum.insert(0,n)
    postWord = [words[0]]

    for i in range(1,len(words)):
        count += 1  # 카운
        if words[i] in postWord or words[i-1][-1] != words[i][0]: #이미 말한 단어이거나, 끝말잇기가 성립하지 않거
            return [peopleNum[count%n],((count-1)//n)+1]
        else:
            postWord.append(words[i]) # 이전단어에 더하고

    return [0,0]

def solution2(n,words):
    for i in range(1,len(words)):
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]: return [(i%n)+1,(i//n)+1]
    else :
        return [0,0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution2(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure","establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
# print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
# 3 ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
# 5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
# "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
# 2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]