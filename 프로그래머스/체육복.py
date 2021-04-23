# 여분을 가지고 왔지만 도난당해서 빌려줄 체육복이 없는 경우를 포함하고,
# 키 포인트는 결국 체육복이 없는 녀석을 찾는거

def solution(n,lost,reserve):
    setLost = set(lost) - set(reserve)
    setReserve = set(reserve) - set(lost)

    for item in setReserve:
        if item-1 in setLost:
            setLost.remove(item-1)
        elif item+1 in setLost:
            setLost.remove(item+1)

    return n-len(setLost)


solution(3,[3],[1])