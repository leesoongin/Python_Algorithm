def solution(phone_number):

    print([1,2]+[3,4])
    return phone_number.replace(phone_number[:-4],'*'*(len(phone_number)-4))

print(solution("01033334444"))


# phone_number	return
# "01033334444"	"*******4444"
# "027778888"	"*****8888"