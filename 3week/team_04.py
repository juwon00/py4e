n = int(input("첫 번쨰 수 입력: ")) # n > 1, m > n
m = int(input("두 번쨰 수 입력: "))

count = 0

for i in range(n,m+1):
    check = 0

    for k in range(1,i+1):
        if i%k == 0:
            check = check + 1

    if check <= 2:
        count = count + 1

print("소수 개수:",count)
