def check_id(num):
    MALE = '남자'
    FEMALE = '여자'

    if num[6] != '-' or len(num) != 14:
        raise Exception

    year = int(num[:2])
    if year <= 21:
        choose = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
        if choose == 'o' and (num[7] == '1' or num[7] == '2'):
          raise Exception
        elif choose == 'x' and (num[7] == '3' or num[7] == '4'):
          raise Exception

    if num[7] == '1' or num[7] == '3':
        gender = MALE
    elif num[7] == '2' or num[7] == '4':
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


# 코치님의 예시 답안
# def check_id(id_number):
#     while True:
#         if len(id_number) != 14 or id_number.find("-") == -1:
#             print("잘못된 번호입니다.")
#             break
        
#         # 21 이하의 숫자로 시작하면 2000년 이후 출생인지 물어보기
#         if int(id_number[:2]) <=21:
#             q = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
#             # 2000년 이후 출생일 때
#             if q == "o":
#                 if id_number[7] not in ["3" ,"4"]:
#                     print("잘못된 번호입니다.")
#                 else:
#                     if id_number[7] == "3":
#                         gender = "남자"
#                     else:
#                         gender = "여자"
#             # 아닐때 1900년 ~ 1921년 사이 출생일 때
#             elif q == "x":
#                 if id_number[7] == "1":
#                     gender = "남자"
#                 else:
#                     gender = "여자"
#             else:
#                 continue
#         # 1922년 ~ 1999년 사이 출생일 때
#         else:
#             if id_number[7] not in ["1" , "2"]:
#                 print("잘못된 번호입니다.")
#             else:
#                 if id_number[7] == "1":
#                     gender = "남자"
#                 else:
#                     gender = "여자"
#         year = id_number[:2]
#         mon = id_number[2:4]
#         try:
#             print(f"{year}년{mon}월 {gender}")
#         except:
#             print("올바른 번호를 넣어주세요")
#         break