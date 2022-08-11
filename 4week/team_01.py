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
