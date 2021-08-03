def solution(price, money, count):
    values = [price *i for i in range(1,count+1)]
    return 0 if money > sum(values) else sum(values) - money