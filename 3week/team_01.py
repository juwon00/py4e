number = int(input("몇 단? : "))
print(number,"단")

i = 1
while True:
    result = number * i

    if result > 50:
        break

    print(number,"X",i,"=",result)
    i = i + 2
