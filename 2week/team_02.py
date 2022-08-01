def year_pay_tax(a):
    if a <= 1200:
        after_tax = a * 0.94
    elif a <= 4600:
        after_tax = a * 0.85
    elif a <= 8800:
        after_tax = a * 0.76
    elif a <= 15000:
        after_tax = a * 0.65
    elif a <= 30000:
        after_tax = a * 0.62
    elif a <= 50000:
        after_tax = a * 0.6
    else:
        after_tax = a * 0.58
    return after_tax

mp = input("monthly_payment = ")
month_pay = int(mp)
year_pay = month_pay * 12

real_year_pay = int(year_pay_tax(year_pay))

print("세전 연봉:", year_pay,"만원")
print("세후 연봉:", real_year_pay,"만원")
