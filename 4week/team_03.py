def wrong_guest_book(file):
    for j in file:
        i = j.split("\n")[0]
        n, m = i.split(",")
        if m[3] != "-" or m[8] != "-" or len(m) != 13 or m[:3] != "010":
            print("잘못 쓴 사람: " + str(n))
            print("잘못 쓴 번호: " + str(m) + "\n")


guest_book = open('guest_book.txt')

wrong_guest_book(guest_book)
