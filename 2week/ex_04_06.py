def computepay(fh, fr):
    if fh > 40:
        overh = fh - 40
        overp = overh * fr * 0.5
        pay = fh * fr + overp
    else:
        pay = fh * fr
    return pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = computepay(fh,fr)

print("Pay:",pay)





# def computepay(hours, rate):
#     if hours > 40:
#         reg = rate * hours
#         otp = (hours - 40.0) * (rate * 0.5)
#         pay = reg + otp
#     else:
#         pay = hours * rate
#     return pay
#
# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# fh = float(sh)
# fr = float(sr)
#
# xp = computepay(fh, fr)
#
# print("Pay: ", xp)
