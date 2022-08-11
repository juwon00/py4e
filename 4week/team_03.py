def wrong_guest_book(file):
    file_path = "guest_book.txt"

    with open(file_path) as f:
        lines = f.read().splitlines()

    print(lines[3:6])
    print(len(lines[1]))



    for i in range(0,len(lines)):
        if len(lines[i]) != 16:
            print(lines[i])



    # for line in file:
    #     line = line.rstrip()
    #     print(line)


        # len(file.readlines()) = 파일전체의 줄 길이
    # print(len(file.readlines()))





guest_book = open('guest_book.txt')

# try:
wrong_guest_book(guest_book)
# except:
#     print("잘못쓴사람:")
