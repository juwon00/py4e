def check_id(num):
    MALE = '남자'
    FEMALE = '여자'

    if num[6] != '-':
        raise Exception
    if len(num) != 14:
        raise Exception

    year = int(num[:2])
    if year <= 21:
        choose = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
        if choose == 'o':
            if num[8] == '1' or num[8] == '2':
                raise Exception
        elif choose == 'x':
            if num[8] == '3' or num[8] == '4':
                raise Exception
        else:
            raise Exception

    if num[8] == '1' or num[8] == '3':
        gender = MALE
    elif num[8] == '2' or num[8] == '4':
        gender = FEMALE
    else:
        raise Exception

    print(num[:2]+'년'+num[2:4]+'월',gender)



a = input("주민등록번호를 입력해주세요: ")
try:
    check_id(a)
except:
    print('잘못된 번호입니다.')
    print('올바른 번호를 입력해주세요.')
