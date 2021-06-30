def solution(m,musicinfos):
    m = convert(m)
    matchList = list()
    for info in musicinfos:
        start , end, name, akbo = info.split(",")
        playTime = calTime(start,end)
        akbo = (convert(akbo))
        akbo = ''.join((list(map(''.join,[akbo[i % len(akbo)] for i in range(playTime)]))))
        if m in akbo:
            matchList.append([name, len(akbo)])

    print(matchList)
    if len(matchList) == 0:
        return "(None)"
    elif len(matchList) == 1:
        return matchList[0][0]
    else:
        return sorted(matchList,key=lambda x:-x[1])[0][0]

def calTime(start,end):
    start = list(map(int,start.split(":")))
    end = list(map(int,end.split(":")))

    return ((end[0] - start[0]) * 60) + (end[1] - start[1])

def convert(s):
    s = ''.join(s)
    return s.replace("C#","c").replace("D#","d").replace("E#","e").replace("F#","f").replace("G#","g").replace("A#","a")
print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))


# m	musicinfos	answer
# "ABCDEFG"	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"HELLO"
# "CC#BCC#BCC#BCC#B"	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	"FOO"
# "ABC"	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"WORLD"
