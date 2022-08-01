n = int(input("첫 번쨰 수 입력: "))
m = int(input("두 번쨰 수 입력: "))

fk = (n + m) / 2
ik = int(fk)

i = n
for find_even_number in range(n,m+1):

    if i%2 == 0:
        print(i,"짝수")
        if i == ik:
            print(ik,"중앙값")

    i = i + 1
