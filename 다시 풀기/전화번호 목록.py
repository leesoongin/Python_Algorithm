def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


def solution2(phone_book):
    d1 = dict()

    for item in phone_book:
        d1[item] = 0
    print(d1)
    for item in phone_book:
        tmp = ""
        for ele in item:
            tmp += ele
            if tmp in d1 and tmp != item:
                return False
    return True
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["abcdef" , "abe", "abc" , "def"]))

print(solution2(["119", "97674223", "1195524421"]))

# 입출력 예제
# phone_book	return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false