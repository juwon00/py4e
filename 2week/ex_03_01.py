hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
    overh = hours - 40
    overp = overh * rate * 0.5
else:
    overp = 0
pay = hours * rate + overp
print("Pay:",pay)




# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# fh = float(sh)
# fr = float(sr)
# # print(fh, fr)
# if fh > 40:
#     # print("Overtime")
#     reg = fr * fh
#     otp = (fh - 40.0) * (fr * 0.5)
#     # print(reg, otp)
#     xp = reg + otp
# else:
#     # print("Regular")
#     xp = fh + fr
# print("Pay:",xp)
