# 소문자, 숫자 - _ . 문자만 사용 가능 / . 은 처음과 끝에 사용불가

# 1단계 대문자 -> 소문자 / lower
# 2단계 사용가능한 문자를 제외하고 나머지 모든 문자 제거
# 3단계 . 가 2번 이상 연속되어있다면 하나로 치환
# 4단계 처음이나 끝에 . 가 있다면 제거
# 5단계 아예 빈 문자열이라면 a를 대입
# 6단계 길이가 16자 이상이면 15까지만 남기고 다 지우기 마지막에 . 이라면 그것도 지우기
# 7단계 길이가 2자 이하라면 길이가 3 이 될때까지 반복해서 붙이기
def deleteUnavailableCharacters(new_id):
    for item in new_id:
        if not item.isalpha() and not item.isdigit() and item != '-' and item != '_' and item != '.':
            new_id = new_id.replace(item, '')
    return new_id


def deleteContinuousDot(new_id):
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    return new_id


def deleteFirstLastDot(new_id):
    if new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id


def solution(new_id):
    answer = ''
    new_id = new_id.lower()  # 1단계
    new_id = deleteUnavailableCharacters(new_id)  # 2단계
    new_id = deleteContinuousDot(new_id)  # 3단계
    new_id = deleteFirstLastDot(new_id)  # 4단계

    if not new_id:
        new_id = 'a'  # 5단계

    if len(new_id) >= 16:  # 6단계
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:  # 7단계
        new_id = new_id + new_id[-1] * (3 - len(new_id))
    answer = new_id
    return answer

