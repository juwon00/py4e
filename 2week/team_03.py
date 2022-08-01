def credit_cal(c):
    if c <= 100 and c >= 95:
        credit = "A+"
    elif c < 95 and c >= 90:
        credit = "A"
    elif c < 90 and c >= 85:
        credit = "B+"
    elif c < 85 and c >= 80:
        credit = "B"
    elif c < 80 and c >= 75:
        credit = "C+"
    elif c < 75 and c >= 70:
        credit = "C"
    elif c < 70 and c >= 65:
        credit = "D+"
    elif c < 65 and c >= 60:
        credit = "D"
    elif c < 60 and c >= 0:
        credit = "F"
    else:
        credit = "Error"
    return credit

name = input("이름을 입력하세요: ")
g = input("점수를 입력하세요: ")
grade = float(g)

print("학생이름:",name)
print("점수:",grade,"점")
print("학점:",credit_cal(grade))
