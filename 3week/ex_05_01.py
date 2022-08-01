count = 0
sum = 0

while True:
    sval = input("Enter a number: ")

    if sval == "done":
        break

    try:
        fval = float(sval)
        count = count + 1
        sum = sum + fval
    except:
        print("Invalid float")

print(sum,count,sum/count)



# num = 0
# tot = 0.0
# while True :
#     sval = input('Enter a number:')
#     if sval == 'done' :
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid input')
#         continue
#
#     num = num + 1
#     tot = tot + fval
#
# print(tot,num,tot/num)
#
