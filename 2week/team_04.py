def fee_calcu(t):
    if t == "카드":
        if age < 8 or age >= 75:
            fee = "무료"
        elif age >= 8 and age < 14:
            fee = "450원"
        elif age >= 14 and age < 20:
            fee = "720원"
        else:
            fee = "1200원"
    elif t == "현금":
        if age < 8 or age >= 75:
            fee = "무료"
        elif age >= 8 and age < 14:
            fee = "450원"
        elif age >= 14 and age < 20:
            fee = "1000원"
        else:
            fee = "1300원"
    return fee

a = input("나이를 입력하세요:")
type = input("현금입니까? 카드입니까? ")

age = int(a)

print("나이:",age,"세")
print("지불유형:",type)
print("버스요금:",fee_calcu(type))
