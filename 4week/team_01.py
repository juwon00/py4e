# print(f"{1000000000:,}")

def make_comma(number):
    # print(",".join())
    n = len(number)

    if n <= 3:
        first_num = number
        last_num = ""
        com_num = 0
    elif n%3 == 0:
        first_num = number[:3] + ','
        last_num = number[3:]
        com_num = len(last_num) // 3 - 1
    elif n%3 == 1:
        first_num = number[:1] + ','
        last_num = number[1:]
        com_num = len(last_num) // 3 - 1
    elif n%3 == 2:
        first_num = number[:2] + ','
        last_num = number[2:]
        com_num = len(last_num) // 3 - 1

    k = len(last_num)

    while com_num != 0:
        i = 0
        last_num = last_num[:k-i-3] + ',' + last_num[k-i-3:]
        i = i + 1
        k = k - 3
        com_num = com_num - 1

    result_num = first_num + last_num

    return result_num


num = input("숫자를 입력해주세요: ")

print(make_comma(num))



# 예시 코드
# def make_comma(number):
#     number = str(number) # int를 str으로 변환
#     length = len(number) # 숫자의 길이
#     num_comma = length // 3 # 3으로 나눠서 찍어야하는 콤마의 개수 구하기
#     if length % 3 ==0: 
#         num_comma = num_comma -1 # 길이가 3으로 나눠질 경우 -1

#     new_number = "" # 새로운 숫자를 담을 변수 생성
#     n = -1 # 인덱스를 거꾸로 가야하기 때문에 -1 
#     while num_comma != 0: # 콤마를 다 찍을 때까지 반복
#         new_number = number[n] + new_number
#         if  n % 3 == 0:
#             new_number = "," + new_number
#             num_comma = num_comma - 1
#         n = n - 1
# 		# 콤마를 다 찍고 남은 앞의 숫자를 더해주면 완성
#     print(number[:n+1]+new_number)