hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if fh > 40:
    overh = fh - 40
    overp = overh * fr * 0.5
else:
    overp = 0

pay = fh * fr + overp
print("Pay:",pay)




# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# try:
#     fh = float(sh)
#     fr = float(sr)
# except:
#     print("Error, please enter numeric input")
#     quit()
# #print(fh, fr)
# if fh > 40 :
# 	#print("Overtime")
# 	reg = fr * fh
# 	otp = (fh - 40.0) * (fr * 0.5)
# 	#print(reg, otp)
# 	xp = reg + otp
# else:
# 	#print("regular")
# 	xp = fh * fr
# print("Pay:", xp)
