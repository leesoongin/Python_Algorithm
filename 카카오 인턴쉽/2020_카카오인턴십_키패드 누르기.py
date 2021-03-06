def solution2(numbers, hand):
    answer = ""
    currentL = '*'
    currentR = '#'

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            currentL = str(number)
            answer += 'L'
        elif number == 3 or number == 6 or number == 9:
            currentR = str(number)
            answer += 'R'
        else:
            if distance(number,currentL) > distance(number,currentR):
                currentR = str(number)
                answer += 'R'
            elif distance(number,currentL) < distance(number,currentR):
                currentL = str(number)
                answer += 'L'
            elif distance(number,currentL) == distance(number,currentR):
                if hand == 'left':
                    currentL = str(number)
                    answer += 'L'
                else :
                    currentR = str(number)
                    answer += 'R'
    return answer

def distance(number,hand):
    pad = {"1":(0,0),"2":(0,1),"3":(0,2),"4":(1,0),"5":(1,1),"6":(1,2),"7":(2,0),"8":(2,1),"9":(2,2),"*":(3,0),"0":(3,1),"#":(3,2)}
    target = pad[str(number)]
    hand = pad[hand]
    return abs(target[0] - hand[0]) + abs(target[1] - hand[1])

# 147 -> 왼손 /  369 -> 오른손 / 2580 ->  왼손오른손 가까운거 만약 거리가 같다면 주 손잡

# 거리 구하기

print(solution2([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution2([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))




def solution(numbers, hand):
    answer = ''
    leftHand = '*'
    rightHand = '#'
    num = [ '123', '456', '789', '*0#']

    for item in numbers:
        if item == 1 or item == 4 or item == 7:
            answer += 'L'; leftHand = str(item)
        elif item == 3 or item == 6 or item == 9:
            answer += 'R'; rightHand = str(item)
        else:
            curLeft, curItem, curRight = findPoint(num,leftHand), findPoint(num,str(item)), findPoint(num,rightHand)
            if distanceTwoPoint(curLeft,curItem) > distanceTwoPoint(curRight,curItem): # 오른쪽이 더 가깝다면
                answer += 'R'; rightHand = str(item)
            elif distanceTwoPoint(curLeft,curItem) < distanceTwoPoint(curRight,curItem): # 왼쪽 더 가깝다면
                answer += 'L'; leftHand = str(item)
            else:
                if hand == 'right':
                    answer += 'R'; rightHand = str(item)
                else:
                    answer += 'L'; leftHand = str(item)

    return answer

def findPoint(arr,target):
    for index, item in enumerate(arr):
        if target in item:
            return [index,item.index(target)]
    return

def distanceTwoPoint(one,two):
    return abs(one[0]-two[0])+abs(one[1]-two[1])

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
# 상하좌우로만 가능
# 1,4,7 일때에는 왼손
# 3,6,9 일때에는 오른손
# 2 5 8 0 일때에는 왼,오른손중 가까운 손가락, but 거리가 같다면 왼손잡이면 왼 / 오른손잡이면 오

# 가까운 손가락이 뭔지 알아야겠네
# 어차피 오른손 왼손은 147 369에서만 놈
# 계속돌면서 마지막으로 눌렸던 왼, 오른놈들의 값을 저장 -> 마지막 위치를 저장하는거지
# 거리는 어떻게 구할까 좌표값으로 해결하면 될듯


# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"